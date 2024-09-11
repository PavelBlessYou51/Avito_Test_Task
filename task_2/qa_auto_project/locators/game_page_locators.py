"""The module contains locators from Game page"""

from selenium.webdriver.common.by import By

PLATFORM_FIELD = (By.XPATH, '(//span[@class="ant-descriptions-item-content"])[6]')
BACK_TO_MAIN_BUTTON = (By.CSS_SELECTOR, "button[type='button']")