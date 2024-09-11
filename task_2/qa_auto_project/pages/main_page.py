"""The module functions for working with Web elements"""

import requests

from task_2.qa_auto_project.pages.base_page import BasePage
from task_2.qa_auto_project.locators import main_page_locators as locators


class MainPage(BasePage):

    def get_amount_of_games(self) -> int:
        response = requests.get(self.url)
        games = response.json()
        return games

    def get_filters_status(self) -> tuple[str, str, str]:
        filters = self.elements_are_visible(locators.FILTERS_STATUS)
        filters_status = tuple(map(lambda elem: elem.text, filters))
        return filters_status

    def get_amount_cards_on_page(self) -> int:
        cards = self.elements_are_visible(locators.GAME_CARDS)
        return len(cards)

    def go_to_last_page(self) -> int:
        element = self.element_is_visible(locators.LAST_PAGINATION_ITEM)
        element.click()
        return int(element.text)
