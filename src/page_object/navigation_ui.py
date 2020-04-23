import allure
from src.page_object.base_page import BasePage, locator_for_platform


class NavigationUI(BasePage):

    _main_menu_button = locator_for_platform({
        'MOBILE_WEB': 'id:mw-mf-main-menu-button'
    })

    _login_button = locator_for_platform({
        'MOBILE_WEB': 'css:ul#p-personal>li>a'
    })

    _rss_list_button = locator_for_platform({
        'ANDROID': 'accessibility_id:Лента',
        'IOS': 'accessibility_id:Explore'
    })

    _my_lists_button = locator_for_platform({
        'ANDROID': 'accessibility_id:Мои списки',
        'IOS': 'accessibility_id:Saved',
        'MOBILE_WEB': 'css:#p-personal>li:nth-child(2)>a'
    })

    _history_button = locator_for_platform({
        'ANDROID': 'accessibility_id:История',
        'IOS': 'accessibility_id:History'
    })

    @allure.step('Нажатие на кнопку "Лента" в навигации')
    def open_rss_list(self):
        super().get_element_and_click(self._rss_list_button)

    @allure.step('Нажатие на кнопку "Мои списки" в навигации')
    def open_my_lists(self):
        super().get_element_and_click(self._my_lists_button)

    @allure.step('Нажатие на кнопку "История" в навигации')
    def open_history(self):
        super().get_element_and_click(self._history_button)

    @allure.step('Открытие меню в Web')
    def open_web_menu(self):
        super().get_element_and_click(self._main_menu_button)

    @allure.step('Переход на страницу авторизации')
    def open_login_page(self):
        super().get_element_and_click(self._login_button)
