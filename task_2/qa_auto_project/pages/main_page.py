"""The module functions for working with Web elements"""
import datetime
import time
import random

from selenium.common import TimeoutException
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

from task_2.qa_auto_project.pages.base_page import BasePage
from task_2.qa_auto_project.locators import main_page_locators as locators, game_page_locators as game_locators


class MainPage(BasePage):

    # ID Cat.1
    def get_filters_status(self) -> tuple[str, str, str]:
        """Returns the status of filters"""
        filters = self.elements_are_visible(locators.FILTERS_STATUS)
        platform, category, sort_by = tuple(map(lambda elem: elem.get_attribute('title'), filters))
        return platform, category, sort_by

    def get_cards_on_page(self, return_count: bool = True) -> int | list:
        """Returns a list of cards on the page or their number"""
        cards = self.elements_are_visible(locators.GAME_CARDS)
        if return_count:
            return len(cards)
        return cards

    def go_to_last_page(self) -> int:
        """Switches to the last page of the pagination and returns its number"""
        element = self.element_is_visible(locators.LAST_PAGINATION_ITEM)
        element.click()
        return int(element.text)

    # ID Cat.2 - Cat.13
    def set_filter(self, filter_type: str, value: str, reverse_filter: bool = True):
        """Sets the filters to the specified position"""
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
            if reverse_filter:
                chosen_filter.send_keys(Keys.ARROW_DOWN)
            else:
                chosen_filter.send_keys(Keys.ARROW_UP)
        chosen_filter.send_keys(Keys.RETURN)

    def go_to_next_page(self, count: int = 1):
        """Switches to the next page"""
        for _ in range(count):
            self.element_is_visible(locators.NEXT_BUTTON).click()

    def go_to_previous_page(self, count: int = 1):
        """Switches to the previous page"""
        for _ in range(count):
            self.element_is_visible(locators.PREVIOUS_BUTTON).click()

    def go_to_next_five_page(self, count: int = 1):
        """Flips through five pages ahead"""
        for _ in range(count):
            self.element_is_visible(locators.NEXT_FIVE_PAGES_BUTTON).click()

    def go_to_previous_five_page(self, count: int = 1):
        """Flips back five pages"""
        for _ in range(count):
            self.element_is_visible(locators.PREVIOUS_FIVE_PAGES_BUTTON).click()

    def get_attribute_of_card(self, attribute: str) -> tuple[str]:
        """Extracts the specified attributes from the game cards located on the current page and returns them in the tuple"""
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
        """Checks the correctness of the selection of the game by genre"""
        flag = True
        while flag:
            tuple_genres = self.get_attribute_of_card('genre')
            result_genres = tuple(map(lambda item: item.split()[1].lower(), tuple_genres))
            if result_genres.count(genre) != len(result_genres):
                flag = False
            else:
                self.go_to_next_page()
        return flag

    def processing_sort_by(self, sort_type: str) -> list[str | datetime.datetime]:
        """Checks whether the games are sorted correctly by the specified parameter"""
        if sort_type == 'alphabetical':
            list_titles = list(self.get_attribute_of_card('title'))
            return list_titles
        else:
            list_dates = self.get_attribute_of_card('release_date')
            result_date = list(
                map(lambda my_date: datetime.datetime.strptime(my_date.split()[2], '%d.%m.%Y'), list_dates))
            return result_date

    def processing_platform(self, platform_type: str) -> bool:
        """Checks the correctness of the selection of games by genre"""
        list_of_platform = list()
        for card in range(len(self.get_cards_on_page(False))):
            list_cards = self.get_cards_on_page(False)
            list_cards[card].click()
            platform = self.element_is_presents(game_locators.PLATFORM_FIELD).text
            list_of_platform.append(platform)
            self.click_on_back_to_main_btn()
        if platform_type == 'PC':
            result = tuple(map(lambda item: 'Windows' in item, list_of_platform))
        else:
            result = tuple(map(lambda item: 'Web Browser' in item, list_of_platform))
        return all(result)

    def check_amount_card_element(self) -> bool:
        """Checks the visibility of the element that determines the number of cards on the page"""
        try:
            element = self.element_is_visible(locators.SELECT_AMOUNT_CARDS)
            return True
        except TimeoutException:
            return False

    # ID Cat.14
    def reset_filtration_by_category(self):
        """Sets and resets filtering"""
        self.set_filter('category', 'strategy')
        self.set_filter('category', 'strategy', False)

    def make_screen(self) -> str:
        """Takes a screenshot and determines the file name and path to it"""
        screen_name = 'screen' + f'-{datetime.date.today()}' + '.png'
        screen_path = self.get_dir_for_screen()
        path = screen_path + '\\' + screen_name
        time.sleep(.5)
        self.get_screen_shot(path)
        return path

    def check_main_page(self) -> bool:
        """Checks that the main page is open"""
        try:
            title = self.element_is_visible(locators.MAIN_PAGE_TITLE)
            return True
        except TimeoutException:
            return False

    # ID Btn.1 - Btn.2
    def click_on_back_to_main_btn(self):
        """Clicks on the button to return to the main page"""
        button = self.element_is_clickable(game_locators.BACK_TO_MAIN_BUTTON)
        self.go_to_element(button)
        button.click()

    def go_into_random_card(self):
        """Opens a randomly selected game card from the current page"""
        cards = self.get_cards_on_page(False)
        randon_card = random.choice(cards)
        randon_card.click()

    # ID Pgn.1 - Pgn.7
    def check_activity_pagination_btn(self, type_button: str) -> str:
        """Checks the activity of pagination buttons"""
        if type_button == 'previous':
            button = self.element_is_presents(locators.NOT_ACTIVE_PREVIOUS_BUTTON)
        else:
            self.go_to_last_page()
            button = self.element_is_presents(locators.NOT_ACTIVE_NEXT_BUTTON)
        disable_status = button.get_attribute('disabled')
        return disable_status

    def get_active_page_number(self) -> int:
        """Returns the norm of the active page"""
        current_page = self.element_is_visible(locators.ACTIVE_PAGE_NUMBER)
        current_page = current_page.get_property('title')
        return int(current_page)

    def pagination_for_pages(self):
        """Navigate to a random page using pagination and returns a list of visited page numbers"""
        iterations = random.randint(3, 10)
        count_pages = iterations
        visited_pages = list()
        while iterations != 0:
            pages = self.elements_are_visible(locators.PAGINATION_ITEMS)
            page = random.choice(pages)
            if "ant-pagination-item-active" not in page.get_attribute('class'):
                page.click()
                visited_pages.append(self.get_active_page_number())
                iterations -= 1
        print(visited_pages)
        return count_pages == len(visited_pages)
