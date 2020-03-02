APPIUM_HOST = 'http://localhost:4444/wd/hub'

MY_APP_ANDROID = '/Users/m.barinov/PycharmProjects/appium/Simulators/Wikipedia_2.7.280-r-2019-04-26_apk-dl.com.apk'

DEVICES = {
    'Pixel Emulator (9.0)': 'emulator-5554'
}

DESIRED_CAPS_ANDROID_RESET = {
    'automationName': 'Appium',
    'platformName': 'Android',
    'platformVersion': '9.0',
    'deviceName': DEVICES['Pixel Emulator (9.0)'],
    'app': MY_APP_ANDROID,
    'unicodeKeyboard': 'true',
    # 'autoWebview': 'true',
    'resetKeyboard': 'true',
    # 'autoLaunch': 'false',
    'disableWindowAnimation': 'true',
    'autoWebviewTimeout': '2000',
    # 'chromedriverExecutable': '/Users/m.barinov/PycharmProjects/appium/Simulators/'
}


DESIRED_CAPS_ANDROID_NO_RESET = {
    'platformName': 'Android',
    'platformVersion': '9',
    'deviceName': DEVICES['Pixel Emulator (9.0)'],
    'app': MY_APP_ANDROID,
    'unicodeKeyboard': 'true',
    'noReset': 'true',
}
