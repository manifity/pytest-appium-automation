import pytest
import allure
from src.credo import Keywords, Users
from src.platform import IS_IOS, IS_ANDROID, IS_MOBILE_WEB
from src.page_object.onboarding_elements import OnboardingElements
from src.page_object.search import Search
from src.page_object.article import Article, ArticlesNames
from src.page_object.navigation_ui import NavigationUI
from src.page_object.my_lists import MyLists
from src.page_object.login import LoginPage
from src.page_object.main import MainPage


@pytest.mark.my_lists
@allure.title('Ex5: Тест: сохранение двух статей')
def test_save_two_articles(appdriver):

    if IS_MOBILE_WEB:
        # LOGIN AS USER
        NavigationUI(appdriver).open_web_menu()
        NavigationUI(appdriver).open_login_page()
        LoginPage(appdriver).login_to_wiki()
        assert MainPage(appdriver).get_welcome_text() == f'Welcome, {Users.username}!'
    else:
        # SKIP ONBOARDING ON IOS/ANDROID
        OnboardingElements(appdriver).press_skip_onboarding_button()

    # FIND THE FIRST ARTICLE
    Search(appdriver).click_to_the_search_field()
    Search(appdriver).input_text_to_the_search_field(Keywords.search_python)

    if IS_IOS or IS_ANDROID:
        # OPEN ARTICLE PAGE
        Search(appdriver).open_programming_language_page()

    # SAVE ARTICLE TO FAVORITES
    Article(appdriver).press_save_article_to_my_list()

    if IS_ANDROID:
        # CREATE USER LIST FOR ARTICLE
        OnboardingElements(appdriver).press_to_got_it_button()  # Нажатие на кнопку "Понятно" в инфо об оффлайн статьях
        Article(appdriver).press_create_new_list()
        Article(appdriver).input_my_list_name()
        Article(appdriver).press_ok_to_create_new_list()

        # RETURN BACK
        for back in range(2):
            appdriver.back()

    elif IS_IOS:
        # RETURN BACK
        Article(appdriver).press_go_back_button()

    # CLEAR SEARCH FIELD
    Search(appdriver).clear_the_search_field()

    # FIND THE SECOND ARTICLE
    Search(appdriver).input_text_to_the_search_field(Keywords.search_java)

    if IS_IOS or IS_ANDROID:
        # OPEN ARTICLE PAGE
        Search(appdriver).open_programming_language_page()

    # SAVE ARTICLE TO FAVORITES
    Article(appdriver).press_save_article_to_my_list()

    # OPEN FAVORITES
    if IS_ANDROID:
        Article(appdriver).open_my_list()
        for back in range(3):
            appdriver.back()
        OnboardingElements(appdriver).press_no_thanks_button_sign_up_pop_up()
    elif IS_IOS:
        Article(appdriver).press_go_back_button()
        Search(appdriver).press_to_cancel_search_button()
    else:
        NavigationUI(appdriver).open_web_menu()

    NavigationUI(appdriver).open_my_lists()

    # CHECK SAVED ARTICLES
    if IS_ANDROID:
        MyLists(appdriver).open_my_list()
    elif IS_IOS:
        OnboardingElements(appdriver).press_no_thanks_button_sign_up_pop_up()

    assert 'Python' in ArticlesNames(appdriver).python_article(), 'Can\'t find Python article in your reading list'
    assert 'Java' in ArticlesNames(appdriver).java_article(), 'Can\'t find Java article in your reading list'

    if IS_IOS or IS_ANDROID:
        # DELETE JAVA ARTICLE WITH SWIPE
        ArticlesNames(appdriver).delete_java_with_swipe()
        assert ArticlesNames(appdriver).java_article_no_shown() is None, 'Java\'s article isn\'t deleted'
    else:
        # UNSTAR ARTICLE
        Article(appdriver).press_save_article_to_my_list()  # метод тот же

        # OPEN WATCHLIST AGAIN AND CHECK DELETED ARTICLE
        NavigationUI(appdriver).open_web_menu()
        NavigationUI(appdriver).open_my_lists()
        assert ArticlesNames(appdriver).java_article_no_shown() is None, 'Java\'s article isn\'t deleted'
