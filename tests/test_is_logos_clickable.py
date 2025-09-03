import allure
from selenium import webdriver
from pages.main_page import MainPage

URL = "https://qa-scooter.praktikum-services.ru/"

class TestLogoClickable:
    
    driver = None
    
    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Firefox()
        
    @allure.step("Открываем страницу Яндекс Самокат")
    def open_page(self):
        self.driver.get(URL)
    
    @allure.step ("Клик по кнопке Заказать")
    def click_order_button(self, page):
        page.click_top_order()
        
    @allure.step("Проверяем клик по тексту Самокат")
    def samokat_click(self,page):
        page.click_samokat_logo()
    
    @allure.step ("Проверяем, что переход на страницу произошел")
    def samokat_visible(self,page):
        assert page.is_samokat_page_visible(), "Страница не отображается"
    
    @allure.step ("Проверяем клик по тексту Яндекс")
    def yandex_click(self,page):
        page.click_yandex_logo()
        
    @allure.step("Проверяем, что открылась страница Дзена")
    def verify_dzen_redirect(self, page):
        page.switch_to_new_tab_and_wait_for_url()
        current_url = page.get_current_url()
        assert "dzen.ru" in current_url, f"Ожидался редирект на Дзен, но открыт URL: {current_url}"
        
    def test_is_logos_samokat_clickable(self):
        self.open_page()
        main_page = MainPage(self.driver)
        self.click_order_button(main_page)
        self.samokat_click(main_page)
        self.samokat_visible(main_page)
        
    def test_is_logo_yandex_clickable(self):
        self.open_page()
        main_page = MainPage(self.driver)
        self.yandex_click(main_page)
        self.verify_dzen_redirect(main_page)

        
    @classmethod
    def teardown_class(cls):
        cls.driver.quit()