import re
import allure
from appium.webdriver.common.mobileby import MobileBy
from src.config import BUNDLE_APP
from src.page_object.base_page import BasePage
from src import credo


class Search(BasePage):

    _search_field_default_text = (MobileBy.XPATH, '//*[contains(@text, "Поиск по Википедии")]')
    _search_field_id = (MobileBy.ID, '%s:id/search_container' % BUNDLE_APP)
    _search_text_field_container_id = (MobileBy.ID, '%s:id/search_src_text' % BUNDLE_APP)
    _cancel_search_button = (MobileBy.ID, '%s:id/search_close_btn' % BUNDLE_APP)
    _empty_message_string = (MobileBy.ID, '%s:id/search_empty_message' % BUNDLE_APP)
    _search_results_list = (MobileBy.XPATH, '//*[@resource-id="%s:id/page_list_item_title"]' % BUNDLE_APP)
    _searched_result_programming_language = (MobileBy.XPATH, f'//*[contains(@text, "{credo.programming_language}")]')

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
        results_list = super().get_elements(self._search_results_list)
        for element in results_list:
            sentence = element.text
            if keyword not in sentence:
                raise
