import allure
from src.page_object.base_page import BasePage
from src import credo


class MyLists(BasePage):

    _reading_list_name = f'android_uiautomator:new UiSelector().text("{credo.my_list_name}")'

    @allure.step('Открытие моего списка')
    def open_my_list(self):
        super().get_element_and_click(self._reading_list_name)
