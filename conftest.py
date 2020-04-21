import pytest
from src import platform


@pytest.fixture()
def appdriver():
    driver = platform.get()
    if platform.IS_MOBILE_WEB:
        driver.get('https://ru.m.wikipedia.org/')
    yield driver
    driver.quit()
