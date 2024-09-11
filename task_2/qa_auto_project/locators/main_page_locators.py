"""The module contains locators from Main page"""

from selenium.webdriver.common.by import By

LAST_PAGINATION_ITEM = (By.XPATH, '(//ul/li[last()-2])[1]/a')
FILTERS_STATUS = (By.CSS_SELECTOR,
                  'div[class="ant-select css-17a39f8 ant-select-single ant-select-show-arrow"] span[class="ant-select-selection-item"]')
GAME_CARDS = (By.CSS_SELECTOR, 'li[class="ant-list-item"]')