import allure
from src.credo import Keywords
from src.config import BUNDLE_APP, BUNDLE_ANDROID
from src.page_object.base_page import BasePage, locator_for_platform


class Article(BasePage):

    _save_article_button = locator_for_platform({
        'ANDROID': 'id:%s:id/article_menu_bookmark' % BUNDLE_APP,
        'IOS': 'accessibility_id:Save for later'
    })

    _create_reading_list_plus_button = 'id:%s:id/create_button' % BUNDLE_APP
    _create_reading_list_name_field = 'id:%s:id/text_input' % BUNDLE_APP
    _create_reading_list_ok_button = 'id:%s:id/button1' % BUNDLE_ANDROID

    _go_back_page_button = locator_for_platform({
        'ANDROID;': 'accessibility_id:Перейти вверх',
        'IOS': 'accessibility_id:Back'
    })

    _reading_list_name = f'android_uiautomator:new UiSelector().text("{Keywords.my_list_name}")'
    _article_title_string = 'xpath:/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/' \
                            'android.widget.FrameLayout/android.widget.FrameLayout/android.widget' \
                            '.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/' \
                            'android.view.ViewGroup/android.webkit.WebView/android.webkit' \
                            '.WebView/android.view.View/android.view.View[1]'

    @allure.step('Нажатие кнопки сохранения в список')
    def press_save_article_to_my_list(self):
        super().get_element_and_click(self._save_article_button)

    @allure.step('Нажатие кнопки "Back" (iOS)')
    def press_go_back_button(self):
        super().get_element_and_click(self._go_back_page_button)

    @allure.step('Нажатие кнопки создания нового списка')
    def press_create_new_list(self):
        super().get_element_and_click(self._create_reading_list_plus_button)

    @allure.step('Ввод названия спика в соответствующее поле')
    def input_my_list_name(self):
        super().get_element(self._create_reading_list_name_field).send_keys(Keywords.my_list_name)

    @allure.step('Подтверждение создания списка')
    def press_ok_to_create_new_list(self):
        super().get_element_and_click(self._create_reading_list_ok_button)

    @allure.step('Открытие созданного списка')
    def open_my_list(self):
        super().get_element_and_click(self._reading_list_name)

    @allure.step('Удаление статьи с помощью свайпа')
    def delete_article_by_swipe(self):
        super().get_element_left_swipe(self._reading_list_name)

    @allure.step('Проверка отображения элемента на странице')
    def assert_element_present(self):
        super().get_element(self._article_title_string)


class ArticlesNames(BasePage):

    _python = locator_for_platform({
        'ANDROID': f'android_uiautomator:new UiSelector().text("{Keywords.search_python}")',
        'IOS': f'xpath://XCUIElementTypeLink[contains(@name, "{Keywords.search_python}")]'
    })

    _java = locator_for_platform({
        'ANDROID': f'android_uiautomator:new UiSelector().text("{Keywords.search_java}")',
        'IOS': f'xpath://XCUIElementTypeLink[contains(@name, "{Keywords.search_java}")]'
    })

    @allure.step('Получение текста статьи (Python)')
    def python_article(self):
        return super().get_element_text(self._python)

    @allure.step('Получение текста статьи (Java)')
    def java_article(self):
        return super().get_element_text(self._java)

    @allure.step('Удаление статьи Java с помощью свайпа')
    def delete_java_with_swipe(self):
        super().get_element_left_swipe(self._java)

    @allure.step('Проверка отсутствия статьи Java на странице')
    def java_article_no_shown(self):
        super().get_no_element(self._java)
