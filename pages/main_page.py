from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class MainPage:

    top_order_button = (By.XPATH, "//button[text()='Заказать'][1]")
    bottom_order_button = (By.XPATH, "//button[text()='Заказать'][last()]")
    samokat_logo = (By.CLASS_NAME, "Header_LogoScooter__3lsAR")
    samokat_picture = (By.CLASS_NAME, "Home_Scooter__3YdJy")
    yandex_logo = (By.CLASS_NAME, "Header_LogoYandex__3TSOI")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def click_top_order(self):
        self.driver.find_element(*self.top_order_button).click()

    def click_bottom_order(self):
        self.driver.execute_script("arguments[0].scrollIntoView();", self.driver.find_element(*self.bottom_order_button))
        self.driver.find_element(*self.bottom_order_button).click()

    def click_samokat_logo(self):
        self.driver.find_element(*self.samokat_logo).click()

    def click_yandex_logo(self):
        self.driver.find_element(*self.yandex_logo).click()
        
    def is_samokat_page_visible(self):
        self.wait.until(EC.presence_of_element_located(self.samokat_picture))
        return True
        
    def get_current_url(self):
        return self.driver.current_url
    
    def switch_to_new_tab_and_wait_for_url(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(lambda d: len(d.window_handles) > 1)
        self.driver.switch_to.window(self.driver.window_handles[-1])
        wait.until(lambda d: d.current_url != "about:blank")
