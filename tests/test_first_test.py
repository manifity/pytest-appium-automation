from src.locators_and_actions import OnboardingPage, MainElements


def test_get_text_from_search_field(appdriver):
    OnboardingPage(appdriver).press_skip_onboarding_button()

    assert MainElements(appdriver).get_text_in_the_search_field() == 'Поиск по Википедии',\
        'Text isn\'t presented in the Search field'
