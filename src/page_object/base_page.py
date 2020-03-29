from appium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ex_cond


class BasePage:

    def __init__(self, driver: webdriver) -> None:
        self._driver = driver

    def get_element(self, locator: tuple, timeout=10):
        return WebDriverWait(self._driver, timeout).until(
            ex_cond.visibility_of_element_located(locator), ' : '.join(locator))

    def get_no_element(self, locator: tuple, timeout=10):
        element = WebDriverWait(self._driver, timeout).until(
            ex_cond.invisibility_of_element_located(locator), ' : '.join(locator))
        if element is None:
            return 'No element found'

    def get_elements(self, locator: tuple, timeout=10):
        return WebDriverWait(self._driver, timeout).until(
            ex_cond.visibility_of_any_elements_located(locator), ' : '.join(locator))

    def get_element_text(self, locator: tuple, timeout=10):
        element = WebDriverWait(self._driver, timeout).until(
            ex_cond.visibility_of_element_located(locator), ' : '.join(locator))
        return element.text

    def get_element_and_click(self, locator: tuple, timeout=10):
        element = WebDriverWait(self._driver, timeout).until(
            ex_cond.visibility_of_element_located(locator), ' : '.join(locator))
        assert element.is_displayed() is True, 'Cannot press to the button'
        return element.click()

    def get_element_left_swipe(self, locator: tuple, timeout=10):
        element = WebDriverWait(self._driver, timeout).until(
            ex_cond.visibility_of_element_located(locator), ' : '.join(locator))
        left_x = element.location['x']
        right_x = left_x + element.size['width']
        upper_y = element.location['y']
        lower_y = upper_y + element.size['height']
        middle_y = (upper_y + lower_y) / 2
        self._driver.swipe(right_x, middle_y, left_x, middle_y, duration=500)
