import allure
from src.page_object.onboarding_elements import OnboardingElements
from src.page_object.search import Search
from src import credo


@allure.title('Ex2: Создание метода')
def test_get_text_from_search_field(appdriver):
    OnboardingElements(appdriver).press_skip_onboarding_button()

    assert Search(appdriver).get_text_in_the_search_field() == 'Поиск по Википедии',\
        'Text isn\'t presented in the Search field'


@allure.title('Ex3: Тест: отмена поиска')
def test_cancel_search(appdriver):
    OnboardingElements(appdriver).press_skip_onboarding_button()
    Search(appdriver).click_to_the_search_field()
    Search(appdriver).input_text_to_the_search_field('Python')

    assert appdriver.find_element_by_android_uiautomator('new UiSelector().text("Python")').text == 'Python', \
        'Search results is different, than request'

    Search(appdriver).press_to_cancel_search_button()

    assert Search(appdriver).get_text_in_the_search_field() == 'Поиск по Википедии',\
        'Text isn\'t presented in the Search field'
    assert Search(appdriver).get_text_in_the_empty_search() == \
        'Ищите и читайте свободную энциклопедию на своём языке', 'Search results aren\'t vanished'


@allure.title('Ex4*: Тест: проверка слов в поиске')
def test_check_word_in_search_results(appdriver, ):
    OnboardingElements(appdriver).press_skip_onboarding_button()
    Search(appdriver).click_to_the_search_field()
    Search(appdriver).input_text_to_the_search_field(credo.search_python)

    Search(appdriver).find_keyword_in_search_results('Python')

