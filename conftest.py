import os
import pytest
from appium import webdriver
from src.config import APPIUM_HOST, DESIRED_CAPS_ANDROID_RESET, DESIRED_CAPS_IOS


@pytest.fixture
def appdriver():
    if os.environ.get('PLATFORM') == 'ANDROID':
        driver = webdriver.Remote(APPIUM_HOST, DESIRED_CAPS_ANDROID_RESET)
        yield driver
        driver.quit()
    else:
        driver = webdriver.Remote(APPIUM_HOST, DESIRED_CAPS_IOS)
        yield driver
        driver.quit()
