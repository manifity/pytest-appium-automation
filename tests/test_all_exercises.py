from src.locators_and_actions import OnboardingElements, MainElements, SearchElements, ArticlePage, BottomBar,\
    ArticlesNames, MyLists


def test_get_text_from_search_field(appdriver):
    OnboardingElements(appdriver).press_skip_onboarding_button()

    assert MainElements(appdriver).get_text_in_the_search_field() == 'Поиск по Википедии',\
        'Text isn\'t presented in the Search field'


def test_cancel_search(appdriver):
    OnboardingElements(appdriver).press_skip_onboarding_button()
    MainElements(appdriver).click_to_the_search_field()
    MainElements(appdriver).input_text_to_the_search_field('Python')

    assert appdriver.find_element_by_android_uiautomator('new UiSelector().text("Python")').text == 'Python', \
        'Search results is different, than request'

    MainElements(appdriver).press_to_cancel_search_button()

    assert MainElements(appdriver).get_text_in_the_search_field() == 'Поиск по Википедии',\
        'Text isn\'t presented in the Search field'
    assert MainElements(appdriver).get_text_in_the_empty_search() == \
        'Ищите и читайте свободную энциклопедию на своём языке', 'Search results aren\'t vanished'


def test_save_two_articles(appdriver):
    # FIND AND SAVE THE FIRST ARTICLE
    OnboardingElements(appdriver).press_skip_onboarding_button()
    MainElements(appdriver).click_to_the_search_field()
    MainElements(appdriver).input_text_to_the_search_field('Python')
    SearchElements(appdriver).open_programming_language_page()

    ArticlePage(appdriver).press_save_article_to_my_list()
    OnboardingElements(appdriver).press_to_got_it_button()  # Нажатие на кнопку "Понятно" в инфо об оффлайн статьях
    ArticlePage(appdriver).press_create_new_list()
    ArticlePage(appdriver).input_my_list_name()
    ArticlePage(appdriver).press_ok_to_create_new_list()

    # FIND AND SAVE THE SECOND ARTICLE
    for back in range(2):
        appdriver.back()

    MainElements(appdriver).clear_the_search_field()
    MainElements(appdriver).input_text_to_the_search_field('Java')
    SearchElements(appdriver).open_programming_language_page()

    ArticlePage(appdriver).press_save_article_to_my_list()
    ArticlePage(appdriver).open_my_list()

    # CHECK SAVED ARTICLES
    for back in range(3):
        appdriver.back()

    OnboardingElements(appdriver).press_no_thanks_button_sign_up_pop_up()   # Нажатие на кнопку "Нет, спасибо" в поп-апе
    BottomBar(appdriver).open_my_lists()
    MyLists(appdriver).open_my_list()

    assert ArticlesNames(appdriver).python_article() == 'Python', 'Can\'t find Python article in your reading list'
    assert ArticlesNames(appdriver).java_article() == 'Java', 'Can\'t find Java article in your reading list'

    # DELETE JAVA ARTICLE WITH SWIPE
    ArticlesNames(appdriver).delete_java_with_swipe()

    assert ArticlesNames(appdriver).java_article_no_shown() is None, 'Java\'s article isn\'t deleted'
