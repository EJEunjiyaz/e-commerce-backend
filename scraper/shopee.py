from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

service = ChromeService(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
driver.get("https://shopee.co.th/%E0%B8%A2%E0%B8%B2%E0%B8%87%E0%B8%99%E0%B8%AD%E0%B8%81%E0%B8%A1%E0%B8%AD%E0%B9%80%E0"
           "%B8%95%E0%B8%AD%E0%B8%A3%E0%B9%8C%E0%B9%84%E0%B8%8B%E0%B8%84%E0%B9%8C-%E0%B8%A2%E0%B8%B2%E0%B8%87%E0%B9"
           "%80%E0%B8%A3%E0%B9%80%E0%B8%94%E0%B8%B5%E0%B8%A2%E0%B8%99-MAXXIS-%E0%B9%84%E0%B8%A1%E0%B9%88%E0%B9%83%E0"
           "%B8%8A%E0%B9%89%E0%B8%A2%E0%B8%B2%E0%B8%87%E0%B9%83%E0%B8%99-%E0%B8%82%E0%B8%AD%E0%B8%9A14-%E0%B8%A5%E0"
           "%B8%B2%E0%B8%A2%E0%B9%80%E0%B8%9E%E0%B8%8A%E0%B8%A3%F0%9F%92%8E-MA3D-%E0%B8%A2%E0%B8%B2%E0%B8%87%E0%B8%A1"
           "%E0%B8%AD%E0%B9%80%E0%B8%95%E0%B8%AD%E0%B8%A3%E0%B9%8C%E0%B9%84%E0%B8%8B%E0%B8%84%E0%B9%8C-%E0%B8%A2%E0"
           "%B8%B2%E0%B8%87%E0%B8%99%E0%B8%AD%E0%B8%81-("
           "%E0%B8%A3%E0%B8%B2%E0%B8%84%E0%B8%B2%E0%B8%95%E0%B9%88%E0%B8%AD1%E0%B9%80%E0%B8%AA%E0%B9%89%E0%B8%99)-i"
           ".61199915.2971951703?sp_atk=fd092ff6-0e4c-4378-9db9-5ad55ed414fb")

# price = driver.find_element(By.XPATH, "//div[contains(@class, '_2v0Hgx')]")

language_dialog = WebDriverWait(driver, timeout=5).until(
    lambda d: d.find_element(By.CLASS_NAME, "shopee-button-outline.shopee-button-outline--primary-reverse "))
language_dialog.click()

# product_name = WebDriverWait(driver, timeout=0.1).until(lambda d: d.find_element(By.CSS_SELECTOR, "div._3g8My- > span"))
# print(product_name.text)

variations = WebDriverWait(driver, timeout=5).until(lambda d: d.find_elements(By.CLASS_NAME, "product-variation"))
for variation in variations:
    print(variation.text)
    variation.click()
    price = WebDriverWait(driver, timeout=5).until(lambda d: d.find_element(By.XPATH, "//div[contains(@class, "
                                                                                      "'_2v0Hgx')]"))
    print(price.text)

# item_name = driver.find_element(By.XPATH, "//div[contains(@class, '_3g8My-')]")
# option = driver.find_element(By.XPATH, "//div[contains(@class, 'flex items-center _3ABAc7')]")
# quantity = driver.find_element(By.XPATH, "//div[contains(@class, 'flex items-center L6Jueq')]")

# print(price.text)
# print(option.text)
# if quantity.text != "จำนวน":
#     print(quantity.text)
