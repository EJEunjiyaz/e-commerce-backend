from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

service = ChromeService(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
driver.get("https://shopee.co.th/Apple-iPhone-13-%E0%B8%AB%E0%B8%99%E0%B9%89%E0%B8%B2%E0%B8%88%E0%B8%AD-6.1-%E0%B8%99"
           "%E0%B8%B4%E0%B9%89%E0%B8%A7-i.287137993.10951724608?sp_atk=f674b50f-08d3-47a2-b7da-ac0606b4f4f7")
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
Collect product name 
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
for i in range(len(variations)):
    variation_dict[available_options[i]] = variations[i].text.split()
print(variation_dict)

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
