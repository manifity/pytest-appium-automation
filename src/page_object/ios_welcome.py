import allure
from src.page_object.base_page import BasePage


class WelcomePage(BasePage):

    _next_onboarding_button = 'xpath://*[@name="Next"]'
    _skip_onboarding_button = 'xpath://*[@name="Skip"]'

    _learn_more_about_wiki_link = 'xpath://*[@name="Learn more about Wikipedia"]'
    _new_ways_to_explore_title = 'accessibility_id:New ways to explore'
    _add_edit_languages_link = 'xpath://*[@name="Add or edit preferred languages"]'
    _learn_data_collected_link = 'xpath://*[@name="Learn more about data collected"]'
    _get_started_button = 'xpath://*[@name="Get started"]'

    @allure.step('Нажатие кнопки "Next" в онбординге (при запуске приложения)')
    def press_next_onboarding_button(self):
        super().get_element_and_click(self._next_onboarding_button)

    @allure.step('Нажатие кнопки "Skip" в онбординге (при запуске приложения)')
    def press_skip_onboarding_button(self):
        super().get_element_and_click(self._skip_onboarding_button)

    @allure.step('Проверка отображения ссылки "Learn more about Wikipedia" на экране')
    def wait_learn_more_about_wiki_link(self):
        super().get_element(self._learn_more_about_wiki_link)

    @allure.step('Проверка отображения заголовка "New ways to explore" на экране')
    def wait_new_ways_to_explore_title(self):
        super().get_element(self._new_ways_to_explore_title)

    @allure.step('Проверка отображения ссылки "Add or edit preferred languages" на экране')
    def wait_add_edit_languages_link(self):
        super().get_element(self._add_edit_languages_link)

    @allure.step('Проверка отображения ссылки "Learn more about data collected" на экране')
    def wait_learn_data_collected_link(self):
        super().get_element(self._learn_data_collected_link)

    @allure.step('Нажатие на кнопку "Get started"')
    def press_get_started_button(self):
        super().get_element_and_click(self._get_started_button)
