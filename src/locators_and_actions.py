from appium.webdriver.common.mobileby import MobileBy
from src.config import BUNDLE_APP
from src.base_page import BasePage


class OnboardingPage(BasePage):
    _skip_onboarding_button = (MobileBy.ID, '%s:id/fragment_onboarding_skip_button' % BUNDLE_APP)

    def press_skip_onboarding_button(self):
        super().get_element_and_click(self._skip_onboarding_button)


class MainElements(BasePage):
    _search_field = (MobileBy.XPATH, '//*[contains(@text, "Поиск по Википедии")]')

    def get_text_in_the_search_field(self):
        return super().get_element_text(self._search_field)
