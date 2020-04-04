APPIUM_HOST = 'http://localhost:4444/wd/hub'

MY_APP_ANDROID = '/Users/m.barinov/PycharmProjects/appium/Simulators/Wikipedia_2.7.280-r-2019-04-26_apk-dl.com.apk'
MY_APP_IOS = '/Users/m.barinov/PycharmProjects/appium/Simulators/Wikipedia.app'
BUNDLE_APP = 'org.wikipedia'
BUNDLE_ANDROID = 'android'

DEVICES = {
    'Pixel Emulator (9.0)': 'emulator-5554'
}

DESIRED_CAPS_ANDROID_RESET = {
    'appPackage': BUNDLE_APP,
    'appActivity': '.main.MainActivity',
    'automationName': 'Appium',
    'platformName': 'Android',
    'platformVersion': '9.0',
    'deviceName': DEVICES['Pixel Emulator (9.0)'],
    'app': MY_APP_ANDROID,
    'unicodeKeyboard': 'true',
    'disableWindowAnimation': 'true',
}


DESIRED_CAPS_ANDROID_NO_RESET = {
    'packageName': BUNDLE_APP,
    'appActivity': '.main.MainActivity',
    'automationName': 'Appium',
    'platformName': 'Android',
    'platformVersion': '9.0',
    'deviceName': DEVICES['Pixel Emulator (9.0)'],
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
    'showIOSLog': 'true'
}
