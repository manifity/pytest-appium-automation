import pytest
from src import platform


@pytest.fixture()
def appdriver():
    driver = platform.get()
    yield driver
    driver.quit()
