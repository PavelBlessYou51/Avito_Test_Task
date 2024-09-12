"""The module contains fixtures for test functions"""

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.webdriver import WebDriver
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture()
def get_driver() -> WebDriver:
    """Creates, opens, returns and closes the browser window"""
    options = Options()
    # options.add_argument('--headless')
    options.add_experimental_option('detach', True)
    driver = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.fixture(
    params=[{'sort_by': 'alphabetical', 'category': 'mmorpg'}, {'category': 'strategy', 'sort_by': 'release_date'},
            {'platform': 'browser', 'category': 'mmorpg', 'sort_by': 'release_date'},
            {'platform': 'browser', 'category': 'strategy'},
            pytest.param({'platform': 'browser', 'category': 'social'}, marks=pytest.mark.skip),
            {'platform': 'browser', 'sort_by': 'alphabetical'}, {'platform': 'PC', 'category': 'strategy'},
            {'platform': 'PC', 'category': 'social', 'sort_by': 'alphabetical'},
            {'platform': 'PC', 'sort_by': 'release_date'}, {'platform': 'PC', 'category': 'mmorpg'},
            {'category': 'social', 'sort_by': 'release_date'}, {'category': 'strategy', 'sort_by': 'alphabetical'}],
    ids=['ID_Cat.2', 'ID_Cat.3', 'ID_Cat.4', 'ID_Cat.5', 'ID_Cat.6', 'ID_Cat.7', 'ID_Cat.8', 'ID_Cat.9', 'ID_Cat.10',
         'ID_Cat.11', 'ID_Cat.12', 'ID_Cat.13'])
def provide_data_for_filters(request):
    """Returns parameters for tests from ID Cat.2 to Cat.13"""
    return request.param

