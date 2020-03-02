import pytest
from appium import webdriver
from src.config import APPIUM_HOST, DESIRED_CAPS_ANDROID_RESET


@pytest.fixture
def appdriver():
    driver = webdriver.Remote(APPIUM_HOST, DESIRED_CAPS_ANDROID_RESET)
    yield driver
    driver.quit()
