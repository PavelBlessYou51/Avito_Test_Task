"""The module functions for working with Web elements"""
from datetime import datetime

from selenium.common import TimeoutException
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

from task_2.qa_auto_project.pages.base_page import BasePage
from task_2.qa_auto_project.locators import main_page_locators as locators, game_page_locators as game_locators


class MainPage(BasePage):

    def get_filters_status(self) -> tuple[str, str, str]:
        filters = self.elements_are_visible(locators.FILTERS_STATUS)
        platform, category, sort_by = tuple(map(lambda elem: elem.get_attribute('title'), filters))
        return platform, category, sort_by

    def get_cards_on_page(self, return_count: bool = True) -> int | list:
        cards = self.elements_are_visible(locators.GAME_CARDS)
        if return_count:
            return len(cards)
        return cards

    def go_to_last_page(self) -> int:
        element = self.element_is_visible(locators.LAST_PAGINATION_ITEM)
        element.click()
        return int(element.text)

    def set_filter(self, filter_type: str, value: str):
        filter_dict = {
            'platform': {
                'locators': (locators.FILTER_BY_PLATFORM, locators.FILTER_BY_PLATFORM_INPUT),
                'not_chosen': 0,
                'browser': 1,
                'PC': 2
            },

            'category': {
                'locators': (locators.FILTER_BY_CATEGORY, locators.FILTER_BY_CATEGORY_INPUT),
                'not_chosen': 0,
                'mmorpg': 1,
                'strategy': 3,
                'social': 7
            },

            'sort_by': {
                'locators': (locators.FILTER_SORT, locators.FILTER_SORT_INPUT),
                'not_chosen': 0,
                'release_date': 1,
                'alphabetical': 3
            }
        }
        self.element_is_presents(filter_dict[filter_type]['locators'][0]).click()
        chosen_filter = self.element_is_presents(filter_dict[filter_type]['locators'][1])
        for _ in range(filter_dict[filter_type][value]):
            chosen_filter.send_keys(Keys.ARROW_DOWN)
        chosen_filter.send_keys(Keys.RETURN)

    def go_to_next_page(self):
        self.element_is_visible(locators.NEXT_BUTTON).click()

    def get_attribute_of_card(self, attribute: str) -> tuple[str]:
        attr_dict = {
            'title': locators.GAME_TITLE,
            'release_date': locators.GAME_RELEASE_DATE,
            'genre': locators.GAME_GENRE
        }
        cards = self.get_cards_on_page(False)
        tuple_of_attr = tuple(
            map(lambda elem: elem.find_element(by=By.CSS_SELECTOR, value=attr_dict[attribute]).text, cards))
        return tuple_of_attr

    def processing_genre(self, genre: str) -> bool:
        flag = True
        while flag:
            tuple_genres = self.get_attribute_of_card('genre')
            result_genres = tuple(map(lambda item: item.split()[1].lower(), tuple_genres))
            if result_genres.count(genre) != len(result_genres):
                flag = False
            else:
                self.go_to_next_page()
        return flag

    def processing_sort_by(self, sort_type: str) -> list[str | datetime]:
        if sort_type == 'alphabetical':
            list_titles = list(self.get_attribute_of_card('title'))
            return list_titles
        else:
            list_dates = self.get_attribute_of_card('release_date')
            result_date = list(map(lambda my_date: datetime.strptime(my_date.split()[2], '%d.%m.%Y'), list_dates))
            return result_date

    def processing_platform(self, platform_type: str):
        list_of_platform = list()
        for card in range(len(self.get_cards_on_page(False))):
            list_cards = self.get_cards_on_page(False)
            list_cards[card].click()
            platform = self.element_is_presents(game_locators.PLATFORM_FIELD).text
            list_of_platform.append(platform)
            button = self.element_is_clickable(game_locators.BACK_TO_MAIN_BUTTON)
            self.go_to_element(button)
            button.click()
        if platform_type == 'PC':
            result = tuple(map(lambda item: 'Windows' in item, list_of_platform))
        else:
            result = tuple(map(lambda item: 'Web Browser' in item, list_of_platform))
        return all(result)

    def check_amount_card_element(self):
        try:
            element = self.element_is_visible(locators.SELECT_AMOUNT_CARDS)
            return True
        except TimeoutException:
            return False
