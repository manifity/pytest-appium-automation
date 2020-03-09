from appium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ex_cond


class BasePage:

    def __init__(self, driver: webdriver) -> None:
        self._driver = driver

    def get_element(self, locator: tuple, timeout=10):
        return WebDriverWait(self._driver, timeout).until(
            ex_cond.visibility_of_element_located(locator), ' : '.join(locator))

    def get_element_text(self, locator: tuple, timeout=10):
        element = WebDriverWait(self._driver, timeout).until(
            ex_cond.visibility_of_element_located(locator), ' : '.join(locator))
        return element.text

    def get_element_and_click(self, locator: tuple, timeout=10):
        element = WebDriverWait(self._driver, timeout).until(
            ex_cond.visibility_of_element_located(locator), ' : '.join(locator))
        return element.click()
