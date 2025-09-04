import allure
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
import data.urls

class MainPage(BasePage):
    top_order_button = (By.XPATH, "//button[text()='Заказать'][1]")
    bottom_order_button = (By.XPATH, "//button[text()='Заказать'][last()]")
    samokat_logo = (By.CLASS_NAME, "Header_LogoScooter__3lsAR")
    yandex_logo = (By.CLASS_NAME, "Header_LogoYandex__3TSOI")
    header_locator = (By.CLASS_NAME, "Home_Header__iJKdX")

    @allure.step("Кликаем по верхней кнопке 'Заказать'")
    def click_top_order(self):
        self.click(self.top_order_button)

    @allure.step("Кликаем по нижней кнопке 'Заказать'")
    def click_bottom_order(self):
        self.scroll_into_view(self.bottom_order_button)
        self.click(self.bottom_order_button)

    @allure.step("Кликаем по логотипу Самокат")
    def click_samokat_logo(self):
        self.click(self.samokat_logo)

    @allure.step("Кликаем по логотипу Яндекс")
    def click_yandex_logo(self):
        self.click(self.yandex_logo)

    @allure.step("Проверяем, что открыта страница Самокат")
    def is_samokat_page_visible(self):
        self.wait_for_element_visible(self.header_locator)
        return True
    
    @allure.step("Проверка редиректа на Яндекс.Дзен")
    def verify_dzen_redirect(self):
        self.switch_to_new_tab_and_wait()
        current_url = self.get_current_url()
        assert data.urls.YANDEX_DZEN_DOMAIN in current_url
