import os
from appium import webdriver
from src import config


def get_env(key, default=None):
    return os.environ.get(key=key, default=default)


def get():
    if IS_ANDROID:
        return webdriver.Remote(
            command_executor=config.APPIUM_HOST,
            desired_capabilities=config.DESIRED_CAPS_ANDROID_RESET
        )
    else:
        return webdriver.Remote(
            command_executor=config.APPIUM_HOST,
            desired_capabilities=config.DESIRED_CAPS_IOS
        )


PLATFORM = get_env('PLATFORM', 'IOS')

IS_ANDROID = PLATFORM == 'ANDROID'
IS_IOS = PLATFORM == 'IOS'
