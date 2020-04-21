from src.page_object.base_page import locator_for_platform


class Keywords:
    my_list_name = 'TEST READING LIST'
    programming_language = locator_for_platform({
        'ANDROID': 'Язык программирования',
        'IOS': '(programming language)'
    })

    search_python = 'Python'
    search_java = 'Java'
    search_gta_title = 'Grand Theft Auto'

    search_gta_description = locator_for_platform({
        'ANDROID': 'Компьютерная игра',
        'IOS': 'action-adventure game',
        'MOBILE_WEB': 'action-adventure game'
    })


class AssertTexts:
    search_in_wiki = locator_for_platform({
        'ANDROID': 'Поиск по Википедии',
        'IOS': 'Search Wikipedia',
        'MOBILE_WEB': 'Search Wikipedia'
    })
