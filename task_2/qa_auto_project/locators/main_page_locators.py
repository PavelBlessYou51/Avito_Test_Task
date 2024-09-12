"""The module contains locators from Main page"""

from selenium.webdriver.common.by import By

# Pagination locators
LAST_PAGINATION_ITEM = (By.XPATH, '(//ul/li[last()-2])[1]/a')
NEXT_BUTTON = (By.CSS_SELECTOR, "li[title='Next Page']")
SELECT_AMOUNT_CARDS = (By.CSS_SELECTOR,
                        "div[class='ant-select ant-pagination-options-size-changer css-17a39f8 ant-select-single ant-select-show-arrow ant-select-show-search']")
NOT_ACTIVE_PREVIOUS_BUTTON = (By.CSS_SELECTOR, "li[title='Previous Page'] button")
NOT_ACTIVE_NEXT_BUTTON = (By.CSS_SELECTOR, "li[title='Next Page'] button")

# Filter locators
FILTERS_STATUS = (By.CSS_SELECTOR,
                  'div[class="ant-select css-17a39f8 ant-select-single ant-select-show-arrow"] span[class="ant-select-selection-item"]')
FILTER_BY_PLATFORM = (By.XPATH, "//input[@id='rc_select_0']/parent::*/following-sibling::span")
FILTER_BY_PLATFORM_INPUT = (By.XPATH, "//input[@id='rc_select_0']")

FILTER_BY_CATEGORY = (By.XPATH, "//input[@id='rc_select_1']/parent::*/following-sibling::span")
FILTER_BY_CATEGORY_INPUT = (By.XPATH, "//input[@id='rc_select_1']")

FILTER_SORT = (By.XPATH, "//input[@id='rc_select_2']/parent::*/following-sibling::span")
FILTER_SORT_INPUT = (By.XPATH, "//input[@id='rc_select_2']")

# Card locators
GAME_CARDS = (By.CSS_SELECTOR, 'li[class="ant-list-item"]')
GAME_TITLE = 'h1[class="ant-typography css-17a39f8"]'
GAME_RELEASE_DATE = 'div[class="ant-space-item"]:nth-of-type(1) div[class="ant-typography css-17a39f8"]'
GAME_GENRE = 'div[class="ant-space-item"]:nth-of-type(3) div[class="ant-typography css-17a39f8"]'

# Main Page locators
MAIN_PAGE_TITLE = (By.XPATH, "//h1[contains(text(), 'Main Page')]")
