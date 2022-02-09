from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

service = ChromeService(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
driver.get("https://shopee.co.th/VICTOR-%E0%B9%84%E0%B8%A1%E0%B9%89%E0%B9%81%E0%B8%9A%E0%B8%94%E0%B8%A1%E0%B8%B4%E0"
           "%B8%99%E0%B8%95%E0%B8%B1%E0%B8%99-Graphite-%E0%B8%84%E0%B8%B8%E0%B8%93%E0%B8%A0%E0%B8%B2%E0%B8%9E%E0%B8"
           "%AA%E0%B8%B9%E0%B8%87%E0%B8%AA%E0%B8%B3%E0%B8%AB%E0%B8%A3%E0%B8%B1%E0%B8%9A%E0%B8%A1%E0%B8%B7%E0%B8%AD%E0"
           "%B9%83%E0%B8%AB%E0%B8%A1%E0%B9%88%E0%B8%96%E0%B8%B6%E0%B8%87%E0%B8%A1%E0%B8%B7%E0%B8%AD%E0%B9%82%E0%B8%9B"
           "%E0%B8%A3-%E0%B8%9E%E0%B8%A3%E0%B9%89%E0%B8%AD%E0%B8%A1%E0%B8%82%E0%B8%B6%E0%B9%89%E0%B8%99%E0%B9%80%E0"
           "%B8%AD%E0%B9%87%E0%B8%99-24%E0%B8%9B%E0%B8%AD%E0%B8%99%E0%B8%94%E0%B9%8C-%E0%B8%9F%E0%B8%A3%E0%B8%B5%E0"
           "%B8%8B%E0%B8%AD%E0%B8%87-i.80229818.1977213011?sp_atk=41cbbfb4-e9ef-42f4-b9c5-fef8debbbb89")

"""
Click Thai language selected at welcome.
"""
language_dialog = WebDriverWait(driver, timeout=5).until(
    lambda d: d.find_element(By.CLASS_NAME, "shopee-button-outline.shopee-button-outline--primary-reverse "))
language_dialog.click()

"""
Collect product name 
"""
product_name = WebDriverWait(driver, timeout=5).until(lambda d: d.find_element(By.CSS_SELECTOR, "div._3g8My- > span"))
print(product_name.text)

"""
Search for available variations.
"""
available_variations = WebDriverWait(driver, timeout=5).until(
    lambda d: d.find_elements(By.XPATH, '//button[@class="product-variation" and @aria-disabled="false"]'))
for variation in available_variations:
    print(variation.text)
    variation.click()
    sleep(1)

    price = WebDriverWait(driver, timeout=5).until(lambda d: d.find_element(By.CLASS_NAME, "_2v0Hgx"))
    print(price.text)

    quantity = driver.find_element(By.CSS_SELECTOR, "div.flex.items-center.L6Jueq")
    print(quantity.text)

# """
# Search for not available variations
# """
# not_available_variations = WebDriverWait(driver, timeout=10).until(
#     lambda d: d.find_elements(By.XPATH, '//button[@class="product-variation.product-variation--disabled" and '
#                                         '@aria-disabled="true"]'))
# for variation in not_available_variations:
#     print(variation.text)
#     print("price = 0, available = 0")

"""
Search shop name
"""
shop_name = WebDriverWait(driver, timeout=5).until(lambda d: d.find_element(By.CLASS_NAME, "_1wVLAc"))
print(shop_name.text)
