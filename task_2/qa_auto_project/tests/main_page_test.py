from audioop import reverse

from task_2.qa_auto_project.pages.main_page import MainPage


class TestCat1:

    def test_filters_status(self, get_driver):
        main_page = MainPage(get_driver)
        main_page.open()
        platform, category, sort_by = main_page.get_filters_status()
        first_page_amount_cards = main_page.get_cards_on_page()
        count_pages = main_page.go_to_last_page()
        last_page_amount_cards = main_page.get_cards_on_page()
        assert (platform, category, sort_by) == ('not chosen', 'not chosen', 'not chosen'), 'Filters were chosen'
        assert first_page_amount_cards + last_page_amount_cards + (count_pages - 2) * 10 == 400, 'Not enough games'


class TestFromCat2ToCat13:

    def test_filter_combinations(self, get_driver, provide_data_for_filters):
        main_page = MainPage(get_driver)
        main_page.open()
        for filter_type, value in provide_data_for_filters.items():
            main_page.set_filter(filter_type, value)
        platform = provide_data_for_filters.get('platform')
        category = provide_data_for_filters.get('category')
        sort_by = provide_data_for_filters.get('sort_by')
        if sort_by:
            result_sort = main_page.processing_sort_by(sort_by)
            if sort_by == 'alphabetical':
                assert result_sort == sorted(result_sort), "Sort by alphabetical didn't work"
            else:
                assert result_sort == sorted(result_sort, reverse=True), "Sort by release date didn't work"
        if platform:
            result_platform = main_page.processing_platform(platform)
            assert result_platform, f"Filter by platform {platform} didn't work"
        if category:
            result_category = main_page.processing_genre(category)
            assert result_category, f"Filter by category {category} didn't work"
        assert main_page.check_amount_card_element(), 'The element has disappeared from the DOM'


class TestCat14:

    def test_reset_filter_by_category(self, get_driver):
        main_page = MainPage(get_driver)
        main_page.open()
        main_page.reset_filtration_by_category()
        main_page.make_screen()
        assert main_page.check_main_page(), 'Main Page not found'

class TestBtn1Btn2:

    def test_back_to_main_btn(self, get_driver):
        main_page = MainPage(get_driver)
        main_page.open()
        main_page.go_into_random_card()
        main_page.click_on_back_to_main_btn()
        assert main_page.check_main_page(), 'Main Page not found'

    def test_back_to_main_btn_with_filters(self, get_driver):
        main_page = MainPage(get_driver)
        main_page.open()
        main_page.set_filter('category', 'strategy')
        main_page.go_into_random_card()
        main_page.click_on_back_to_main_btn()
        platform, category, sort_by = main_page.get_filters_status()
        assert (platform, category, sort_by) != ('not chosen', 'not chosen', 'not chosen'), 'The filters have been disabled'