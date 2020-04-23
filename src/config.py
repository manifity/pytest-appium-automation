APPIUM_HOST = 'http://localhost:4445/wd/hub'

MY_APP_ANDROID = '/Users/m.barinov/PycharmProjects/appium/Simulators/wiki.apk'
MY_APP_IOS = '/Users/m.barinov/PycharmProjects/appium/Simulators/Wikipedia.app'
BUNDLE_APP = 'org.wikipedia'
BUNDLE_ANDROID = 'android'

DESIRED_CAPS_ANDROID_RESET = {
    'appPackage': BUNDLE_APP,
    'appActivity': '.main.MainActivity',
    'automationName': 'Appium',
    'platformName': 'Android',
    'platformVersion': '10',
    'deviceName': 'emulator-5554',
    'app': MY_APP_ANDROID,
    'unicodeKeyboard': 'true',
    'disableWindowAnimation': 'true',
}

DESIRED_CAPS_ANDROID_NO_RESET = {
    'packageName': BUNDLE_APP,
    'appActivity': '.main.MainActivity',
    'automationName': 'Appium',
    'platformName': 'Android',
    'platformVersion': '10',
    'deviceName': 'emulator-5554',
    'app': MY_APP_ANDROID,
    'unicodeKeyboard': 'true',
    'disableWindowAnimation': 'true',
    'noReset': 'true',
}

DESIRED_CAPS_IOS = {
    'platformName': 'iOS',
    'platformVersion': '13.3',
    'automationName': 'XCUITest',
    'deviceName': 'iPhone 8',
    'app': MY_APP_IOS,
}

DESIRED_CAPS_MOBILE_WEB = {
    'platformName': 'iOS',
    'platformVersion': '13.3',
    'browserName': 'safari',
    'deviceName': 'iPhone 8',
}

# DESIRED_CAPS_MOBILE_WEB = {
#     'platformName': 'Android',
#     'platformVersion': '10',
#     'deviceName': 'emulator-5554',
#     'automationName': 'Appium',
#     'browserName': 'Chrome'
# }
