import allure
from selenium import webdriver
from pages.main_page import MainPage
from data import urls


class TestLogoClickable:

    driver = None   
   

    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Firefox()
        cls.page = MainPage(cls.driver)
        

    @allure.title("Проверка кликабельности логотипа Самокат")
    def test_is_logos_samokat_clickable(self):
        self.page.open(urls.BASE_URL)
        self.page.click_top_order()
        self.page.click_samokat_logo()
        self.page.is_samokat_page_visible()
        current_url = self.page.get_current_url()
        assert urls.BASE_URL in current_url, (
            f"Ожидался возврат на {urls.BASE_URL}, но текущий URL: {current_url}"
        )

    @allure.title("Проверка кликабельности логотипа Яндекс и редиректа на Дзен")
    def test_is_logo_yandex_clickable(self):
        self.page.open(urls.BASE_URL)
        self.page.click_top_order()
        self.page.click_yandex_logo()
        self.page.verify_dzen_redirect() #Ассерт добавлен в метод verify_dzen_redirect
     
    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
