import allure
from src.config import BUNDLE_APP
from src.page_object.base_page import BasePage
from src import credo


class Search(BasePage):

    _search_field_default_text = 'xpath://*[contains(@text, "Поиск по Википедии")]'
    _search_field_id = 'id:%s:id/search_container' % BUNDLE_APP
    _search_text_field_container_id = 'id:%s:id/search_src_text' % BUNDLE_APP
    _cancel_search_button = 'id:%s:id/search_close_btn' % BUNDLE_APP
    _empty_message_string = 'id:%s:id/search_empty_message' % BUNDLE_APP
    _search_results_list_title = 'xpath://*[@resource-id="%s:id/page_list_item_title"]' % BUNDLE_APP
    _search_results_list_description = 'xpath://*[@resource-id="%s:id/page_list_item_description"]' % BUNDLE_APP
    _search_results_list_all = 'xpath://android.widget.TextView'
    _searched_result_programming_language = f'xpath://*[contains(@text, "{credo.programming_language}")]'

    @allure.step('Получение текста из поля поиска')
    def get_text_in_the_search_field(self):
        return super().get_element_text(self._search_field_default_text)

    @allure.step('Клик в поле поиска')
    def click_to_the_search_field(self):
        super().get_element_and_click(self._search_field_default_text)

    @allure.step('Ввод текста в поле поиска')
    def input_text_to_the_search_field(self, text):
        super().get_element(self._search_text_field_container_id).send_keys(text)

    @allure.step('Очистка поля поиска')
    def clear_the_search_field(self):
        super().get_element(self._search_text_field_container_id).clear()

    @allure.step('Нажатие кнопки "Х" в поле поиска')
    def press_to_cancel_search_button(self):
        super().get_element_and_click(self._cancel_search_button)

    @allure.step('Получение текста заглушки, при отсутствии результатов поиска')
    def get_text_in_the_empty_search(self):
        return super().get_element_text(self._empty_message_string)

    @allure.step('Нажатие на элемент с текстом "Язык программирования"')
    def open_programming_language_page(self):
        super().get_element_and_click(self._searched_result_programming_language)

    @allure.step('Поиск ключевого слова во всех видимых результатах поиска')
    def find_keyword_in_search_results(self, keyword):
        results_list = super().get_elements(self._search_results_list_title)

        for element in results_list:
            sentence = element.text
            if keyword not in sentence:
                raise

    @allure.step('Проверка, что название и описание статьи есть минимум в 3-х результатах поиска')
    def wait_for_element_by_title_and_description(self, title, description):
        results_list = super().get_elements(self._search_results_list_all)
        title_count = 0
        description_count = 0

        for title_keyword in results_list:
            result = title_keyword.text
            if title in result:
                title_count += 1

        for description_keyword in results_list:
            result = description_keyword.text
            if description in result:
                description_count += 1

        assert title_count >= 3, 'Title results are less than 3'
        assert description_count >= 3, 'Description results are less than 3'
