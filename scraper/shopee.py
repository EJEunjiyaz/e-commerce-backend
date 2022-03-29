from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

service = ChromeService(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
driver.get("https://shopee.co.th/Apple-iPhone12-%E0%B8%AB%E0%B8%99%E0%B9%89%E0%B8%B2%E0%B8%88%E0%B8%AD-6.1-%E0%B8%99"
           "%E0%B8%B4%E0%B9%89%E0%B8%A7-i.287137993.7862109494?sp_atk=cbb0583f-e97e-4e1e-b9bb-e6ccd583927c&xptdk"
           "=cbb0583f-e97e-4e1e-b9bb-e6ccd583927c")
# driver.get("https://shopee.co.th/Apple-Watch-Series-7-GPS-("
#            "2021)-%E0%B8%AA%E0%B8%B2%E0%B8%A2-Sport-Band-i.287137993.11167901407")
# driver.get("https://shopee.co.th/%E0%B8%9B%E0%B8%B2%E0%B8%81%E0%B8%81%E0%B8%B2%E0%B8%84%E0%B8%A7%E0%B8%AD%E0%B8%99%E0"
#            "%B8%95%E0%B8%B1%E0%B9%89%E0%B8%A1-Marshmallow-0.29-%E0%B8%A1%E0%B8%A1.-%E0%B8%AB%E0%B8%A1%E0%B8%B6%E0%B8"
#            "%81%E0%B8%AA%E0%B8%B5%E0%B8%99%E0%B9%89%E0%B8%B3%E0%B9%80%E0%B8%87%E0%B8%B4%E0%B8%99-("
#            "1%E0%B8%94%E0%B9%89%E0%B8%B2%E0%B8%A1)-i.87642797.5502488788?sp_atk=0fda7e23-1cf6-429e-b80b-95c28c20d59e"
#            "&xptdk=0fda7e23-1cf6-429e-b80b-95c28c20d59e")
print("Load Shopee item successful.")


def query_price(obj):
    price_div = obj.find_element(By.CLASS_NAME, "_2v0Hgx")
    price = int(''.join(filter(str.isdigit, price_div.text)))
    return price


def query_product_image(obj):
    image_div = obj.find_element(By.CLASS_NAME, "_3rslob")
    style = image_div.get_attribute("style")
    text = style.split('"', 1)[1].split('"', 1)[0]
    return text


def query_rating_score(obj):
    span = obj.find_element(By.CLASS_NAME, 'product-rating-overview__rating-score')
    return span.text


def query_rating_voter(obj):
    div_text = obj.find_elements(By.CLASS_NAME, '_3uBhVI')[1].text
    if "พัน" in div_text:
        rating_voter = int(float(div_text.replace("พัน", "")) * 1000)
    else:
        rating_voter = int(div_text)
    return rating_voter


def query_product_sold(obj):
    div_text = obj.find_element(By.CLASS_NAME, '_3b2Btx').text
    if "พัน" in div_text:
        product_sold = int(float(div_text.replace("พัน", "")) * 1000)
    else:
        product_sold = int(div_text)
    return product_sold


def query_store_name(obj):
    div = obj.find_element(By.CLASS_NAME, '_1wVLAc')
    return div.text


def query_store_link(obj):
    a = obj.find_element(By.CLASS_NAME, '_3IIjTV')
    store_link = a.get_attribute('href')
    return store_link


def query_store_avatar(obj):
    div = obj.find_element(By.CLASS_NAME, '_2T4rHi')
    img = div.find_element(By.CLASS_NAME, 'shopee-avatar__img')
    img_link = img.get_attribute('src')
    return img_link


"""Click Thai language selected at welcome."""
print("Start to select language dialog.")
language_dialog = WebDriverWait(driver, timeout=5).until(
    lambda d: d.find_element(By.CLASS_NAME, "shopee-button-outline.shopee-button-outline--primary-reverse "))
language_dialog.click()
print("Click language dialog successful.")

"""Collect product name."""
product_name = WebDriverWait(driver, timeout=5).until(lambda d: d.find_element(By.CSS_SELECTOR, "div._3g8My- > span"))
print(product_name.text)

"""Collect product image."""
image = query_product_image(driver)
print(image)

"""Collect store name."""
store_name = query_store_name(driver)
print(store_name)

"""Collect store link."""
store_link = query_store_link(driver)
print(store_link)

"""Collect store avatar."""
store_avatar = query_store_avatar(driver)
print(store_avatar)

"""Collect rating score."""
rating_score = query_rating_score(driver)
print(rating_score)

"""Collect rating voter."""
rating_voter = query_rating_voter(driver)
print(rating_voter)

"""Collect product sold."""
product_sold = query_product_sold(driver)
print(product_sold)


"""
Search for available variations.
"""
options = WebDriverWait(driver, timeout=5).until(lambda d: d.find_elements(By.XPATH, '//label[@class="koZBMj"]'))
default_options = ["ช้อปเพิ่มคุ้มกว่า", "การจัดส่ง"]
"""available_options for user to custom their own variations."""
available_options = []

for option in options:
    if option.text not in default_options:
        available_options.append(option.text)
print(available_options)

"""Create dict to store the options and variations"""
variation_dict = {}
variations = driver.find_elements(by=By.CLASS_NAME, value='_3ABAc7')


"""Check number of variations then scraping."""
if len(available_options) == 2:  # If the product has 2 variations.
    variation1 = variations[0]
    variation2 = variations[1]

    # variation_dict[available_options[i]] = variation.text.split("\n")  # Insert into dict
    for button1 in variation1.find_elements(by=By.TAG_NAME, value='button'):
        button1.click()
        """Check the button is clickable or not."""
        try:
            select1 = variation1.find_element(by=By.CLASS_NAME, value='product-variation--selected')
            if select1.text == button1.text:
                """Loop over second variation"""
                for button2 in variation2.find_elements(by=By.TAG_NAME, value='button'):
                    button2.click()
                    try:
                        select2 = variation2.find_element(by=By.CLASS_NAME, value='product-variation--selected')
                        if select2.text == button2.text:
                            quantity_div = driver.find_element(by=By.CLASS_NAME, value='L6Jueq')
                            quantity = int(''.join(filter(str.isdigit, quantity_div.text)))
                            price = query_price(driver)
                            print(button1.text, button2.text, quantity, price)
                    except Exception:
                        print(button1.text, button2.text, 0, None)
                    button2.click()
        except Exception:
            for button2 in variation2.find_elements(by=By.TAG_NAME, value='button'):
                print(button1.text, button2.text, 0, None)
elif len(available_options) == 1:  # If the product has only variation.
    variation = variations[0]
    for button in variation.find_elements(by=By.TAG_NAME, value='button'):
        button.click()
        """Check the button is clickable or not."""
        try:
            select = variation.find_element(by=By.CLASS_NAME, value='product-variation--selected')
            if select.text == button.text:
                quantity_div = driver.find_element(by=By.CLASS_NAME, value='L6Jueq')
                quantity = int(''.join(filter(str.isdigit, quantity_div.text)))
                price = query_price(driver)
                print(button.text, quantity, price)
            else:
                print(button.text, 0, None)
        except Exception:
            print("Button unavailable")
        button.click()
# print(variation_dict)


"""
Search shop name
"""
# shop_name = WebDriverWait(driver, timeout=5).until(lambda d: d.find_element(By.CLASS_NAME, "_1wVLAc"))
# print(shop_name.text)
