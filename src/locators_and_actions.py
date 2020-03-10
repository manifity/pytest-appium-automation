from appium.webdriver.common.mobileby import MobileBy
from src.config import BUNDLE_APP
from src.base_page import BasePage


class OnboardingPage(BasePage):
    _skip_onboarding_button = (MobileBy.ID, '%s:id/fragment_onboarding_skip_button' % BUNDLE_APP)

    def press_skip_onboarding_button(self):
        super().get_element_and_click(self._skip_onboarding_button)


class MainElements(BasePage):
    _search_field_default_text = (MobileBy.XPATH, '//*[contains(@text, "Поиск по Википедии")]')
    _search_field_id = (MobileBy.ID, '%s:id/search_container' % BUNDLE_APP)
    _search_text_field_container_id = (MobileBy.ID, '%s:id/search_src_text' % BUNDLE_APP)
    _cancel_search_button = (MobileBy.ID, '%s:id/search_close_btn' % BUNDLE_APP)
    _empty_message_string = (MobileBy.ID, '%s:id/search_empty_message' % BUNDLE_APP)

    def get_text_in_the_search_field(self):
        return super().get_element_text(self._search_field_default_text)

    def click_to_the_search_field(self):
        super().get_element_and_click(self._search_field_default_text)

    def input_text_to_the_search_field(self, text):
        super().get_element(self._search_text_field_container_id).send_keys(text)

    def press_to_cancel_search_button(self):
        super().get_element_and_click(self._cancel_search_button)

    def get_text_in_the_empty_search(self):
        return super().get_element_text(self._empty_message_string)
