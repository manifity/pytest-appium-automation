from appium.webdriver.common.mobileby import MobileBy
from src.config import BUNDLE_APP, BUNDLE_ANDROID
from src.base_page import BasePage


class OnboardingElements(BasePage):

    _skip_onboarding_button = (MobileBy.ID, '%s:id/fragment_onboarding_skip_button' % BUNDLE_APP)
    _offline_article_got_it_button = (MobileBy.ID, '%s:id/onboarding_button' % BUNDLE_APP)
    _sig_in_pop_up_no_button = (MobileBy.ID, '%s:id/button2' % BUNDLE_ANDROID)

    def press_skip_onboarding_button(self):
        super().get_element_and_click(self._skip_onboarding_button)

    def press_to_got_it_button(self):
        super().get_element_and_click(self._offline_article_got_it_button)

    def press_no_thanks_button_sign_up_pop_up(self):
        super().get_element_and_click(self._sig_in_pop_up_no_button)


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

    def clear_the_search_field(self):
        super().get_element(self._search_text_field_container_id).clear()

    def press_to_cancel_search_button(self):
        super().get_element_and_click(self._cancel_search_button)

    def get_text_in_the_empty_search(self):
        return super().get_element_text(self._empty_message_string)


class SearchElements(BasePage):

    _search_results_list = (MobileBy.ANDROID_UIAUTOMATOR,
                            'new UiSelector().resourceId("org.wikipedia:id/search_results_list")')
    _searched_result_programming_language = (MobileBy.ANDROID_UIAUTOMATOR,
                                             'new UiSelector().text("Язык программирования")')

    def open_programming_language_page(self):
        super().get_element_and_click(self._searched_result_programming_language)


class ArticlePage(BasePage):

    _save_article_button = (MobileBy.ID, '%s:id/article_menu_bookmark' % BUNDLE_APP)
    _create_reading_list_plus_button = (MobileBy.ID, '%s:id/create_button' % BUNDLE_APP)
    _create_reading_list_name_field = (MobileBy.ID, '%s:id/text_input' % BUNDLE_APP)
    _create_reading_list_ok_button = (MobileBy.ID, '%s:id/button1' % BUNDLE_ANDROID)
    _go_back_page_button = (MobileBy.ACCESSIBILITY_ID, 'Перейти вверх')

    _reading_list_name = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("TEST READING LIST")')

    def press_save_article_to_my_list(self):
        super().get_element_and_click(self._save_article_button)

    def press_create_new_list(self):
        super().get_element_and_click(self._create_reading_list_plus_button)

    def input_my_list_name(self):
        super().get_element(self._create_reading_list_name_field).send_keys('TEST READING LIST')

    def press_ok_to_create_new_list(self):
        super().get_element_and_click(self._create_reading_list_ok_button)

    def open_my_list(self):
        super().get_element_and_click(self._reading_list_name)

    def delete_article_by_swipe(self):
        super().get_element_left_swipe(self._reading_list_name)


class BottomBar(BasePage):

    _rss_list_button = (MobileBy.ACCESSIBILITY_ID, 'Лента')
    _my_lists_button = (MobileBy.ACCESSIBILITY_ID, 'Мои списки')
    _history_button = (MobileBy.ACCESSIBILITY_ID, 'История')

    def open_rss_list(self):
        super().get_element_and_click(self._rss_list_button)

    def open_my_lists(self):
        super().get_element_and_click(self._my_lists_button)

    def open_history(self):
        super().get_element_and_click(self._history_button)


class ArticlesNames(BasePage):

    _python = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Python")')
    _java = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Java")')

    def python_article(self):
        return super().get_element_text(self._python)

    def java_article(self):
        return super().get_element_text(self._java)

    def delete_java_with_swipe(self):
        super().get_element_left_swipe(self._java)

    def java_article_no_shown(self):
        super().get_no_element(self._java)


class MyLists(BasePage):

    _reading_list_name = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("TEST READING LIST")')

    def open_my_list(self):
        super().get_element_and_click(self._reading_list_name)
