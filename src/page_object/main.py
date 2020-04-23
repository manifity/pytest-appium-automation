import allure
from src.page_object.base_page import BasePage, locator_for_platform


class MainPage(BasePage):

    _welcome_user_message = locator_for_platform({
        'MOBILE_WEB': 'css:main#content h1#section_0'
    })

    @allure.step('Получение текста с приветствием пользователя')
    def get_welcome_text(self):
        return super().get_element_text(self._welcome_user_message)
