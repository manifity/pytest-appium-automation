import allure
from src.page_object.base_page import BasePage, locator_for_platform
from src.credo import Users
from time import sleep


class LoginPage(BasePage):

    _login_field = locator_for_platform({
        'MOBILE_WEB': 'id:wpName1'
    })

    _password_field = locator_for_platform({
        'MOBILE_WEB': 'id:wpPassword1'
    })

    _login_button = locator_for_platform({
        'MOBILE_WEB': 'id:wpLoginAttempt'
    })

    @allure.step('')
    def login_to_wiki(self):
        super().get_element(self._login_field).send_keys(Users.username)
        super().get_element(self._password_field).send_keys(Users.password)
        super().get_element_and_click(self._login_button)
        sleep(5)
