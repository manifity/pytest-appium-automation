import allure
from src.config import BUNDLE_APP, BUNDLE_ANDROID
from src.page_object.base_page import BasePage, locator_for_platform


class OnboardingElements(BasePage):

    _skip_onboarding_button = locator_for_platform({
        'ANDROID': 'id:%s:id/fragment_onboarding_skip_button' % BUNDLE_APP,
        'IOS': 'xpath://XCUIElementTypeButton[@name="Skip"]'
    })

    _offline_article_got_it_button = locator_for_platform({
        'ANDROID': 'id:%s:id/onboarding_button' % BUNDLE_APP,
    })

    _sign_in_pop_up_no_button = locator_for_platform({
        'ANDROID': 'id:%s:id/button2' % BUNDLE_ANDROID,
        'IOS': 'accessibility_id:Close'
    })

    @allure.step('Нажатие кнопки "Пропустить" в онбординге (при запуске приложения)')
    def press_skip_onboarding_button(self):
        super().get_element_and_click(self._skip_onboarding_button)

    @allure.step('Нажатие кнопки "Понятно" в окне информировании об оффлайн статьях')
    def press_to_got_it_button(self):
        super().get_element_and_click(self._offline_article_got_it_button)

    @allure.step('Нажатие кнопки "Нет, спасибо" в окне предложения зарегистрироваться')
    def press_no_thanks_button_sign_up_pop_up(self):
        super().get_element_and_click(self._sign_in_pop_up_no_button)
