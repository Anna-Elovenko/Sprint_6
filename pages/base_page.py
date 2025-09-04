from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver, timeout=15):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def open(self, url):
        self.driver.get(url)

    def find(self, locator):
        return self.driver.find_element(*locator)

    def click(self, locator):
        self.wait_for_element_clickable(locator).click()

    def send_keys(self, locator, value, clear=False):
        element = self.wait_for_element_visible(locator)
        if clear:
            element.clear()
        element.send_keys(value)

    def wait_for_element_visible(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    def wait_for_element_present(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator))

    def wait_for_element_clickable(self, locator):
        return self.wait.until(EC.element_to_be_clickable(locator))

    def get_current_url(self):
        return self.driver.current_url

    def scroll_into_view(self, locator):
        element = self.find(locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def switch_to_new_tab_and_wait(self):
        self.wait.until(lambda d: len(d.window_handles) > 1)
        self.driver.switch_to.window(self.driver.window_handles[-1])
        self.wait.until(lambda d: d.current_url != "about:blank")
