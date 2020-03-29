import allure
from src.page_object.onboarding_elements import OnboardingElements
from src.page_object.search import Search


@allure.title('Ex6: Тест: assert title')
def test_assert_title(appdriver):
    OnboardingElements(appdriver).press_skip_onboarding_button()
    Search(appdriver).click_to_the_search_field()
    Search(appdriver).input_text_to_the_search_field('Python')
    Search(appdriver).open_programming_language_page()

    assert appdriver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/'
                                           'android.widget.FrameLayout/android.widget.FrameLayout/android.widget'
                                           '.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/'
                                           'android.view.ViewGroup/android.webkit.WebView/android.webkit.WebView/'
                                           'android.view.View/android.view.View[1]').is_displayed()
