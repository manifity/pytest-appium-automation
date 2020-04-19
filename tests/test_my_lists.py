import pytest
import allure
from src.credo import Keywords
from src.platform import IS_ANDROID
from src.page_object.onboarding_elements import OnboardingElements
from src.page_object.search import Search
from src.page_object.article import Article, ArticlesNames
from src.page_object.navigation_ui import NavigationUI
from src.page_object.my_lists import MyLists


@pytest.mark.my_lists
@allure.title('Ex5: Тест: сохранение двух статей')
def test_save_two_articles(appdriver):
    # FIND AND SAVE THE FIRST ARTICLE
    OnboardingElements(appdriver).press_skip_onboarding_button()
    Search(appdriver).click_to_the_search_field()
    Search(appdriver).input_text_to_the_search_field(Keywords.search_python)
    Search(appdriver).open_programming_language_page()

    Article(appdriver).press_save_article_to_my_list()
    if IS_ANDROID:
        OnboardingElements(appdriver).press_to_got_it_button()  # Нажатие на кнопку "Понятно" в инфо об оффлайн статьях
        Article(appdriver).press_create_new_list()
        Article(appdriver).input_my_list_name()
        Article(appdriver).press_ok_to_create_new_list()

        # FIND AND SAVE THE SECOND ARTICLE
        for back in range(2):
            appdriver.back()
    else:
        Article(appdriver).press_go_back_button()

    Search(appdriver).clear_the_search_field()
    Search(appdriver).input_text_to_the_search_field(Keywords.search_java)
    Search(appdriver).open_programming_language_page()

    Article(appdriver).press_save_article_to_my_list()

    if IS_ANDROID:
        Article(appdriver).open_my_list()
        for back in range(3):
            appdriver.back()
        OnboardingElements(appdriver).press_no_thanks_button_sign_up_pop_up()

    else:
        Article(appdriver).press_go_back_button()
        Search(appdriver).press_to_cancel_search_button()

    # CHECK SAVED ARTICLES
    NavigationUI(appdriver).open_my_lists()
    if IS_ANDROID:
        MyLists(appdriver).open_my_list()
    else:
        OnboardingElements(appdriver).press_no_thanks_button_sign_up_pop_up()

    assert 'Python' in ArticlesNames(appdriver).python_article(), 'Can\'t find Python article in your reading list'
    assert 'Java' in ArticlesNames(appdriver).java_article(), 'Can\'t find Java article in your reading list'

    # DELETE JAVA ARTICLE WITH SWIPE
    ArticlesNames(appdriver).delete_java_with_swipe()

    assert ArticlesNames(appdriver).java_article_no_shown() is None, 'Java\'s article isn\'t deleted'
