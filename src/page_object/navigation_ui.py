import allure
from appium.webdriver.common.mobileby import MobileBy
from src.page_object.base_page import BasePage


class NavigationUI(BasePage):

    _rss_list_button = (MobileBy.ACCESSIBILITY_ID, 'Лента')
    _my_lists_button = (MobileBy.ACCESSIBILITY_ID, 'Мои списки')
    _history_button = (MobileBy.ACCESSIBILITY_ID, 'История')

    @allure.step('Нажатие на кнопку "Лента" в навигации')
    def open_rss_list(self):
        super().get_element_and_click(self._rss_list_button)

    @allure.step('Нажатие на кнопку "Мои списки" в навигации')
    def open_my_lists(self):
        super().get_element_and_click(self._my_lists_button)

    @allure.step('Нажатие на кнопку "История" в навигации')
    def open_history(self):
        super().get_element_and_click(self._history_button)
