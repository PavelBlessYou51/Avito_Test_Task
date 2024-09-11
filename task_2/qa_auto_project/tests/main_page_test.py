from task_2.qa_auto_project.pages.main_page import MainPage

class TestCat1:

    def test_filters_status(self, get_driver):
        main_page = MainPage(get_driver)
        main_page.open()
        status = main_page.get_filters_status()
        assert status == ('not chosen', 'not chosen', 'not chosen'), 'Filters were chosen'

    def test_amount_game(self, get_driver):
        main_page = MainPage(get_driver)
        first_page_amount_cards = main_page.get_amount_cards_on_page()
        count_pages = main_page.go_to_last_page()
        last_page_amount_cards = main_page.get_amount_cards_on_page()
        assert first_page_amount_cards + last_page_amount_cards + (count_pages - 2) * 10 == 400, 'Not enough games'
