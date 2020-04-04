import allure
from src.config import BUNDLE_APP, BUNDLE_ANDROID
from src.page_object.base_page import BasePage


class OnboardingElements(BasePage):

    _skip_onboarding_button = 'id:%s:id/fragment_onboarding_skip_button' % BUNDLE_APP
    _offline_article_got_it_button = 'id:%s:id/onboarding_button' % BUNDLE_APP
    _sig_in_pop_up_no_button = 'id:%s:id/button2' % BUNDLE_ANDROID

    @allure.step('Нажатие кнопки "Пропустить" в онбординге (при запуске приложения)')
    def press_skip_onboarding_button(self):
        super().get_element_and_click(self._skip_onboarding_button)

    @allure.step('Нажатие кнопки "Понятно" в окне информировании об оффлайн статьях')
    def press_to_got_it_button(self):
        super().get_element_and_click(self._offline_article_got_it_button)

    @allure.step('Нажатие кнопки "Нет, спасибо" в окне предложения зарегистрироваться')
    def press_no_thanks_button_sign_up_pop_up(self):
        super().get_element_and_click(self._sig_in_pop_up_no_button)
