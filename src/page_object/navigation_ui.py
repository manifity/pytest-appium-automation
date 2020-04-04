import allure
from src.page_object.base_page import BasePage


class NavigationUI(BasePage):

    _rss_list_button = 'accessibility_id:Лента'
    _my_lists_button = 'accessibility_id:Мои списки'
    _history_button = 'accessibility_id:История'

    @allure.step('Нажатие на кнопку "Лента" в навигации')
    def open_rss_list(self):
        super().get_element_and_click(self._rss_list_button)

    @allure.step('Нажатие на кнопку "Мои списки" в навигации')
    def open_my_lists(self):
        super().get_element_and_click(self._my_lists_button)

    @allure.step('Нажатие на кнопку "История" в навигации')
    def open_history(self):
        super().get_element_and_click(self._history_button)
