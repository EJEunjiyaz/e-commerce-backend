from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

service = ChromeService(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
# driver.get("https://shopee.co.th/Apple-iPhone-13-%E0%B8%AB%E0%B8%99%E0%B9%89%E0%B8%B2%E0%B8%88%E0%B8%AD-6.1-%E0%B8%99"
#            "%E0%B8%B4%E0%B9%89%E0%B8%A7-i.287137993.10951724608?sp_atk=f674b50f-08d3-47a2-b7da-ac0606b4f4f7")
driver.get("https://shopee.co.th/%F0%9F%9A%9A%E0%B8%AA%E0%B9%88%E0%B8%87%E0%B8%82%E0%B8%AD%E0%B8%87%E0%B8%97%E0%B8%B8"
           "%E0%B8%81%E0%B8%A7%E0%B8%B1%E0%B8%99-%E0%B8%81%E0%B8%B2%E0%B8%87%E0%B9%80%E0%B8%81%E0%B8%87%E0%B8%A7%E0"
           "%B8%B4%E0%B8%99%E0%B9%80%E0%B8%97%E0%B8%88%E0%B8%97%E0%B8%A3%E0%B8%87%E0%B8%8A%E0%B9%88%E0%B8%B2%E0%B8%87"
           "-%E0%B9%80%E0%B8%AD%E0%B8%A726-32-%E0%B8%A1%E0%B8%B5%E0%B9%84%E0%B8%8B%E0%B8%95%E0%B9%8C%E0%B8%88%E0%B8"
           "%B1%E0%B8%A1%E0%B9%82%E0%B8%9A%E0%B9%89%E0%B8%94%E0%B9%89%E0%B8%A7%E0%B8%A2%E0%B8%99%E0%B8%B0%E0%B8%84%E0"
           "%B8%B0-%E0%B9%80%E0%B8%AA%E0%B8%B7%E0%B9%89%E0%B8%AD%E0%B8%9C%E0%B9%89%E0%B8%B2%E0%B9%81%E0%B8%9F%E0%B8"
           "%8A%E0%B8%B1%E0%B9%88%E0%B8%99-%E0%B8%AA%E0%B8%B8%E0%B8%94%E0%B8%AE%E0%B8%B4%E0%B8%95-i.151206650"
           ".4157186287?sp_atk=2215c8ac-cd93-40d7-9970-fa30f2308c9a&xptdk=2215c8ac-cd93-40d7-9970-fa30f2308c9a")
print("Load Shopee item successful.")

"""
Click Thai language selected at welcome.
"""
print("Start to select language dialog.")
language_dialog = WebDriverWait(driver, timeout=5).until(
    lambda d: d.find_element(By.CLASS_NAME, "shopee-button-outline.shopee-button-outline--primary-reverse "))
language_dialog.click()
print("Click language dialog successful.")

"""
Collect product name.
"""
product_name = WebDriverWait(driver, timeout=5).until(lambda d: d.find_element(By.CSS_SELECTOR, "div._3g8My- > span"))
print(product_name.text)

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
                            print(button1.text, button2.text, quantity)
                    except Exception:
                        print("Button 2 unavailable")
                    button2.click()
        except Exception:
            print("Button 1 unavailable")
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
                print(button.text, quantity)
            else:
                print(button.text, 0)
        except Exception:
            print("Button unavailable")
# print(variation_dict)

# available_variations = WebDriverWait(driver, timeout=5).until(
#     lambda d: d.find_elements(By.XPATH, '//button[@class="product-variation" and @aria-disabled="false"]'))
# for variation in available_variations:
#     print(variation.text)
#     variation.click()
#     sleep(1)
#
#     price = WebDriverWait(driver, timeout=5).until(lambda d: d.find_element(By.CLASS_NAME, "_2v0Hgx"))
#     print(price.text)
#
#     quantity = driver.find_element(By.CSS_SELECTOR, "div.flex.items-center.L6Jueq")
#     print(quantity.text)

"""
Search for not available variations
"""
# not_available_variations = WebDriverWait(driver, timeout=10).until(
#     lambda d: d.find_elements(By.XPATH, '//button[@class="product-variation.product-variation--disabled" and '
#                                         '@aria-disabled="true"]'))
# for variation in not_available_variations:
#     print(variation.text)
#     print("price = 0, available = 0")

"""
Search shop name
"""
# shop_name = WebDriverWait(driver, timeout=5).until(lambda d: d.find_element(By.CLASS_NAME, "_1wVLAc"))
# print(shop_name.text)
