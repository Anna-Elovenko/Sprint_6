import allure
from selenium import webdriver
from pages.main_page import MainPage
from data import urls
from pages.base_page import BasePage


class TestLogoClickable:

    driver = None   
   

    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Firefox()
        cls.base_page = BasePage(cls.driver)
        cls.main_page = MainPage(cls.driver)
        

    @allure.title("Проверка кликабельности логотипа Самокат")
    def test_is_logos_samokat_clickable(self):
        self.base_page.open(urls.BASE_URL)
        self.main_page.click_top_order()
        self.main_page.click_samokat_logo()
        self.main_page.is_samokat_page_visible()
        

    @allure.title("Проверка кликабельности логотипа Яндекс и редиректа на Дзен")
    def test_is_logo_yandex_clickable(self):
        self.base_page.open(urls.BASE_URL)
        self.main_page.click_top_order()
        self.main_page.click_yandex_logo()
        self.main_page.verify_dzen_redirect()
        
        
    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
