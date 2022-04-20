from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager


def query_price(obj):
    price_div = obj.find_element(By.CLASS_NAME, "_2v0Hgx")
    price = ''.join(filter(str.isdigit, price_div.text))
    return price


def query_product_image(obj):
    image_div = obj.find_element(By.CLASS_NAME, "_3rslob")
    style = image_div.get_attribute("style")
    text = style.split('"', 1)[1].split('"', 1)[0]
    return text


def query_rating_score(obj):
    div = obj.find_element(By.CLASS_NAME, '_3uBhVI')
    return div.text


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


def shopee_scrape_variation(url):
    service = ChromeService(executable_path=ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.get(url)
    print("Load Shopee item successful.")

    """Click Thai language selected at welcome."""
    print("Start to select language dialog.")
    language_dialog = WebDriverWait(driver, timeout=5).until(
        lambda d: d.find_element(By.CLASS_NAME, "shopee-button-outline.shopee-button-outline--primary-reverse "))
    language_dialog.click()
    print("Click language dialog successful.")

    """Collect product name."""
    product_name = WebDriverWait(driver, timeout=5).until(
        lambda d: d.find_element(By.CSS_SELECTOR, "div._3g8My- > span")).text
    # print(product_name)

    """
    Search for available variations.
    """
    options = WebDriverWait(driver, timeout=5).until(lambda d: d.find_elements(By.XPATH, '//label[@class="koZBMj"]'))
    default_options = ["ช้อปเพิ่มคุ้มกว่า", "การจัดส่ง", ""]
    """available_options for user to custom their own variations."""
    available_options = []

    for option in options:
        if option.text not in default_options:
            available_options.append(option.text)
    # print(available_options)

    """Create dict to store the options and variations"""
    variations_list = []
    variations = driver.find_elements(by=By.CLASS_NAME, value='_3ABAc7')

    """Check number of variations then scraping."""
    if len(available_options) == 2:  # If the product has 2 variations.
        variation1 = variations[0]
        variation2 = variations[1]

        # print(variation1.text)
        # print(variation2.text)
        return product_name, available_options, variation1.text.split(), variation2.text.split()


def shopee_scrape(url):
    service = ChromeService(executable_path=ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.get(url)
    print("Load Shopee item successful.")

    """Click Thai language selected at welcome."""
    print("Start to select language dialog.")
    language_dialog = WebDriverWait(driver, timeout=5).until(
        lambda d: d.find_element(By.CLASS_NAME, "shopee-button-outline.shopee-button-outline--primary-reverse "))
    language_dialog.click()
    print("Click language dialog successful.")

    """Collect product name."""
    product_name = WebDriverWait(driver, timeout=5).until(
        lambda d: d.find_element(By.CSS_SELECTOR, "div._3g8My- > span")).text
    # print(product_name)

    """Collect product image."""
    product_image = query_product_image(driver)
    # print(product_image)

    """Collect store name."""
    store_name = query_store_name(driver)
    # print(store_name)

    """Collect store link."""
    store_link = query_store_link(driver)
    # print(store_link)

    """Collect store avatar."""
    store_avatar = query_store_avatar(driver)
    # print(store_avatar)

    """Collect rating score."""
    rating_score = query_rating_score(driver)
    # print(rating_score)

    """Collect rating voter."""
    rating_voter = query_rating_voter(driver)
    # print(rating_voter)

    """Collect product sold."""
    product_sold = query_product_sold(driver)
    # print(product_sold)

    """
    Search for available variations.
    """
    options = WebDriverWait(driver, timeout=5).until(lambda d: d.find_elements(By.XPATH, '//label[@class="koZBMj"]'))
    default_options = ["ช้อปเพิ่มคุ้มกว่า", "การจัดส่ง", ""]
    """available_options for user to custom their own variations."""
    available_options = []

    for option in options:
        if option.text not in default_options:
            available_options.append(option.text)
    # print(available_options)

    """Create dict to store the options and variations"""
    variations_list = []
    variations = driver.find_elements(by=By.CLASS_NAME, value='_3ABAc7')

    # print(available_options)

    """Check number of variations then scraping."""
    if len(available_options) == 2:  # If the product has 2 variations.
        variation1 = variations[0]
        variation2 = variations[1]

        for button1 in variation1.find_elements(by=By.TAG_NAME, value='button'):
            button1.click()
            """Check the button is clickable or not."""
            try:
                select1 = variation1.find_element(by=By.CLASS_NAME, value='product-variation--selected')
                if select1.text == button1.text:
                    """Loop over second variation"""
                    for button2 in variation2.find_elements(by=By.TAG_NAME, value='button'):
                        button2.click()
                        sleep(0.2)
                        try:
                            select2 = variation2.find_element(by=By.CLASS_NAME, value='product-variation--selected')
                            if select2.text == button2.text:
                                quantity_div = driver.find_element(by=By.CLASS_NAME, value='L6Jueq')
                                quantity = ''.join(filter(str.isdigit, quantity_div.text))
                                price = query_price(driver)
                                # print(button1.text, button2.text, quantity, price)
                                """Create dictionary and add product information."""
                                variation_dict = {
                                    available_options[0]: button1.text,
                                    available_options[1]: button2.text,
                                    "quantity": quantity,
                                    "price": price
                                }
                                variations_list.append(variation_dict)
                        except Exception:
                            # print(button1.text, button2.text, 0, "null")
                            variation_dict = {
                                available_options[0]: button1.text,
                                available_options[1]: button2.text,
                                "quantity": "0",
                                "price": "null"
                            }
                            variations_list.append(variation_dict)
                        button2.click()
            except Exception:
                for button2 in variation2.find_elements(by=By.TAG_NAME, value='button'):
                    # print(button1.text, button2.text, 0, "null")
                    variation_dict = {
                        available_options[0]: button1.text,
                        available_options[1]: button2.text,
                        "quantity": "0",
                        "price": "null"
                    }
                    variations_list.append(variation_dict)
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
                    print(button.text, "0", "null")
            except Exception:
                print("Button unavailable")
            button.click()

    driver.close()

    return product_name, product_image, store_name, store_link, store_avatar, variations_list, rating_score, rating_voter, product_sold


# product = {
#     "name": product_name,
#     "image": product_image,
#     "store": {
#         "name": store_name,
#         "link": store_link,
#         "avatar": store_avatar
#     },
#     "created_at": datetime.now(),
#     "variations": variations_list,
#     "rating": {
#         "avg_star": rating_score,
#         "voter": rating_voter
#     },
#     "sold": product_sold
# }
#
# product_json = json.dumps(product, cls=DjangoJSONEncoder, ensure_ascii=False)
# print(product_json)

# print(shopee_scrape(
#     "https://shopee.co.th/%E0%B9%80%E0%B8%AA%E0%B8%B7%E0%B9%89%E0%B8%AD%E0%B9%80%E0%B8%8A%E0%B8%B4%E0%B9%89%E0"
#     "%B8%95%E0%B9%80%E0%B8%81%E0%B8%B2%E0%B8%AB%E0%B8%A5%E0%B8%B5-%E0%B9%81%E0%B8%82%E0%B8%99%E0%B8%AA%E0%B8"
#     "%B1%E0%B9%89%E0%B8%99%E0%B8%9C%E0%B8%B9%E0%B9%89%E0%B8%AB%E0%B8%8D%E0%B8%B4%E0%B8%87-%E0%B8%AA%E0%B8%B5"
#     "%E0%B8%9E%E0%B8%B7%E0%B9%89%E0%B8%99-%E0%B8%9C%E0%B9%89%E0%B8%B2%E0%B8%99%E0%B8%B4%E0%B9%88%E0%B8%A1%E0"
#     "%B8%99%E0%B8%B8%E0%B9%88%E0%B8%A1-%E0%B9%80%E0%B8%9A%E0%B8%B2-%E0%B9%83%E0%B8%AA%E0%B9%88%E0%B8%AA%E0%B8"
#     "%9A%E0%B8%B2%E0%B8%A2-%E0%B9%84%E0%B8%A1%E0%B9%88%E0%B8%95%E0%B9%89%E0%B8%AD%E0%B8%87%E0%B8%A3%E0%B8%B5"
#     "%E0%B8%94%E0%B8%81%E0%B9%87%E0%B9%83%E0%B8%AA%E0%B9%88%E0%B9%84%E0%B8%94%E0%B9%89-%E0%B8%9C%E0%B9%89%E0"
#     "%B8%B2%E0%B9%84%E0%B8%A1%E0%B9%88%E0%B8%A2%E0%B8%B1%E0%B8%9A-i.16489766.14938034833?sp_atk=35102125-2034"
#     "-40ad-afd7-acc088019733"))

# shopee_scrape_variation("https://shopee.co.th/%E0%B8%9C%E0%B9%89%E0%B8%B2%E0%B8%AB%E0%B9%88%E0%B8%A1%E0%B8%AA%E0%B8%AD%E0%B8%94%E0%B9%81%E0%B8%82%E0%B8%99-(%E0%B8%82%E0%B8%99%E0%B8%B2%E0%B8%94-50x58-%E0%B8%99%E0%B8%B4%E0%B9%89%E0%B8%A7-%E0%B8%9C%E0%B9%89%E0%B8%B2%E0%B8%99%E0%B8%B8%E0%B9%88%E0%B8%A1%E0%B8%A1%E0%B8%B2%E0%B8%81)-Blanket-with-Sleeve-%E0%B8%9C%E0%B9%89%E0%B8%B2%E0%B8%AB%E0%B9%88%E0%B8%A1%E0%B8%A1%E0%B8%B5%E0%B9%81%E0%B8%82%E0%B8%99-%E0%B8%9C%E0%B9%89%E0%B8%B2%E0%B8%AB%E0%B9%88%E0%B8%A1%E0%B8%81%E0%B8%B1%E0%B8%99%E0%B8%AB%E0%B8%99%E0%B8%B2%E0%B8%A7-%E0%B8%9C%E0%B9%89%E0%B8%B2%E0%B8%84%E0%B8%A5%E0%B8%B8%E0%B8%A1-%E0%B9%80%E0%B8%AA%E0%B8%B7%E0%B9%89%E0%B8%AD%E0%B8%81%E0%B8%B1%E0%B8%99%E0%B8%AB%E0%B8%99%E0%B8%B2%E0%B8%A7-%E0%B8%9C%E0%B9%89%E0%B8%B2%E0%B8%AB%E0%B9%88%E0%B8%A1%E0%B8%AA%E0%B8%A7%E0%B8%A1%E0%B9%81%E0%B8%82%E0%B8%99-i.74577230.7803295221?sp_atk=b93c2ae1-9137-41b0-9c20-d32297d098c9&xptdk=b93c2ae1-9137-41b0-9c20-d32297d098c9")

# var = [
#     {
#         "name": "ผ้าห่มสอดแขน (ขนาด 50x58 นิ้ว, ผ้านุ่มมาก) / Blanket with Sleeve ผ้าห่มมีแขน ผ้าห่มกันหนาว ผ้าคลุม เสื้อกันหนาว ผ้าห่มสวมแขน"
#     },
#     {
#         "key": "สี",
#         "value": ["สีฟ้า", "สีส้ม", "สีครีม"]
#     },
#     {
#         "key": "ปัก",
#         "value": ["ปักชื่อ", "ไม่ปักชื่อ"]
#     }
# ]
