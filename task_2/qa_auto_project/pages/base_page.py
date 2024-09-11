"""The module contains basic methods for working with pages of site"""
from selenium.webdriver.ie.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver: WebDriver, url: str):
        self.driver = driver
        self.url = url

    def open(self):
        self.driver.get(self.url)

    # Methods for seeking elements on the web-page

    def element_is_visible(self, locator: tuple[str, str], timeout: int = 5) -> WebElement:
        return WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))

    def elements_are_visible(self, locator: tuple[str, str], timeout: int = 5) -> list[WebElement]:
        return WebDriverWait(self.driver, timeout).until(EC.visibility_of_all_elements_located(locator))

    def go_to_element(self, element: WebElement):
        self.driver.execute_script("return arguments[0].scrollIntoView(true);", element)