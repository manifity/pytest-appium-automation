import pytest
import allure
from src.platform import IS_IOS
from src.page_object.ios_welcome import WelcomePage


@allure.title('Ex10: Настройка работы на iOS')
@pytest.mark.skipif(IS_IOS, reason='Get started test for iOS only')
def test_get_started(appdriver):

    WelcomePage(appdriver).wait_learn_more_about_wiki_link()
    WelcomePage(appdriver).press_next_onboarding_button()

    WelcomePage(appdriver).wait_new_ways_to_explore_title()
    WelcomePage(appdriver).press_next_onboarding_button()

    WelcomePage(appdriver).wait_add_edit_languages_link()
    WelcomePage(appdriver).press_next_onboarding_button()

    WelcomePage(appdriver).wait_learn_data_collected_link()
    WelcomePage(appdriver).press_get_started_button()
