import pytest
import allure
from src.credo import Keywords
from src.platform import IS_ANDROID
from src.page_object.onboarding_elements import OnboardingElements
from src.page_object.search import Search


@pytest.mark.search
@allure.title('Ex2: Создание метода')
def test_get_text_from_search_field(appdriver):
    OnboardingElements(appdriver).press_skip_onboarding_button()

    if IS_ANDROID:
        assert Search(appdriver).get_text_in_the_search_field() == 'Поиск по Википедии',\
            'Text isn\'t presented in the Search field'
    else:
        assert Search(appdriver).get_text_in_the_search_field() == 'Search Wikipedia',\
            'Text isn\'t presented in the Search field'


@pytest.mark.search
@allure.title('Ex3: Тест: отмена поиска')
def test_cancel_search(appdriver):
    OnboardingElements(appdriver).press_skip_onboarding_button()
    Search(appdriver).click_to_the_search_field()
    Search(appdriver).input_text_to_the_search_field('Python')

    assert 'Python' in Search(appdriver).get_text_from_the_searched_result(), \
        'Can\'t find Python article in your reading list'

    Search(appdriver).press_to_clear_search_button()

    if IS_ANDROID:
        assert Search(appdriver).get_text_in_the_search_field() == 'Поиск по Википедии',\
            'Text isn\'t presented in the Search field'
        assert Search(appdriver).get_text_in_the_empty_search() == \
            'Ищите и читайте свободную энциклопедию на своём языке', 'Search results aren\'t vanished'
    else:
        assert Search(appdriver).get_text_in_the_search_field() == 'Search Wikipedia',\
            'Text isn\'t presented in the Search field'


@pytest.mark.search
@allure.title('Ex4*: Тест: проверка слов в поиске')
def test_check_word_in_search_results(appdriver):
    OnboardingElements(appdriver).press_skip_onboarding_button()
    Search(appdriver).click_to_the_search_field()
    Search(appdriver).input_text_to_the_search_field(Keywords.search_python)

    Search(appdriver).find_keyword_in_search_results('Python')


@pytest.mark.search
@allure.title('Ex9*: Рефакторинг темплейта')
def test_check_word_in_search_results(appdriver):
    OnboardingElements(appdriver).press_skip_onboarding_button()
    Search(appdriver).click_to_the_search_field()
    Search(appdriver).input_text_to_the_search_field(Keywords.search_gta_title)

    Search(appdriver).wait_for_element_by_title_and_description(
        Keywords.search_gta_title, Keywords.search_gta_description)

