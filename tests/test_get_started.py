import pytest
import allure
from src.platform import IS_ANDROID
from src.page_object.ios_welcome import WelcomePage


@pytest.mark.get_started
@pytest.mark.skipif(IS_ANDROID, reason='Get started test for iOS only')
@allure.title('Ex10: Настройка работы на iOS')
def test_get_started(appdriver):

    WelcomePage(appdriver).wait_learn_more_about_wiki_link()
    WelcomePage(appdriver).press_next_onboarding_button()

    WelcomePage(appdriver).wait_new_ways_to_explore_title()
    WelcomePage(appdriver).press_next_onboarding_button()

    WelcomePage(appdriver).wait_add_edit_languages_link()
    WelcomePage(appdriver).press_next_onboarding_button()

    WelcomePage(appdriver).wait_learn_data_collected_link()
    WelcomePage(appdriver).press_get_started_button()
