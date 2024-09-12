"""The module contains basic methods for working with pages of site"""
import os

from selenium.webdriver.ie.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.url = 'https://makarovartem.github.io/frontend-avito-tech-test-assignment/'

    def open(self):
        """Opens the page"""
        self.driver.get(self.url)

    # Methods for seeking elements on the web-page
    def element_is_visible(self, locator: tuple[str, str], timeout: int = 5) -> WebElement:
        """Checks the visibility of an element on the page"""
        return WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))

    def elements_are_visible(self, locator: tuple[str, str], timeout: int = 5) -> list[WebElement]:
        """Checks the visibility of an elements on the page"""
        return WebDriverWait(self.driver, timeout).until(EC.visibility_of_all_elements_located(locator))

    def element_is_presents(self, locator: tuple[str, str], timeout: int = 5) -> WebElement:
        """Checks the presence of an element in the DOM"""
        return WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(locator))

    def elements_are_present(self, locator: tuple[str, str], timeout: int = 5) -> list[WebElement]:
        """Checks the presence of an elements in the DOM"""
        return WebDriverWait(self.driver, timeout).until(EC.presence_of_all_elements_located(locator))

    def element_is_clickable(self, locator: tuple[str, str], timeout: int = 5) -> WebElement:
        """Checks the clickability of the button"""
        return WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable(locator))

    def go_to_element(self, element: WebElement):
        """Moves the cursor to element"""
        self.driver.execute_script("return arguments[0].scrollIntoView(true);", element)

    def get_screen_shot(self, path: str):
        """Makes a screenshot"""
        self.driver.get_screenshot_as_file(path)

    def get_dir_for_screen(self) -> str:
        """Make path to save screenshot"""
        root_dir = os.getcwd() + '\\task_2\\qa_auto_project\\screenshots\\'
        os.makedirs(root_dir, exist_ok=True)
        return root_dir