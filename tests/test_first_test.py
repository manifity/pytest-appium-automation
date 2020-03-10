from src.locators_and_actions import OnboardingPage, MainElements


def test_get_text_from_search_field(appdriver):
    OnboardingPage(appdriver).press_skip_onboarding_button()

    assert MainElements(appdriver).get_text_in_the_search_field() == 'Поиск по Википедии',\
        'Text isn\'t presented in the Search field'


def test_cancel_search(appdriver):
    OnboardingPage(appdriver).press_skip_onboarding_button()
    MainElements(appdriver).click_to_the_search_field()
    MainElements(appdriver).input_text_to_the_search_field('Python')

    assert appdriver.find_element_by_android_uiautomator('new UiSelector().text("Python")').text == 'Python', \
        'Search results is different, than request'

    MainElements(appdriver).press_to_cancel_search_button()

    assert MainElements(appdriver).get_text_in_the_search_field() == 'Поиск по Википедии',\
        'Text isn\'t presented in the Search field'
    assert MainElements(appdriver).get_text_in_the_empty_search() == \
        'Ищите и читайте свободную энциклопедию на своём языке', 'Search results aren\'t vanished'
