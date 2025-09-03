import allure
import pytest
from selenium import webdriver
from pages.main_page import MainPage
from pages.order_page import OrderPage

URL = "https://qa-scooter.praktikum-services.ru/"

order_data = [
    {
        "first_name": "Наташа",
        "last_name": "Смирнова",
        "address": "ул. Мира, 10",
        "station": "Казанская",
        "phone": "891234567890",
        "date": "05.09.2025",
        "comment": "Позвонить за 20 минут"
    },
    {
        "first_name": "Игорь",
        "last_name": "Наумов",
        "address": "ул. Красная, 17",
        "station": "Центральная",
        "phone": "899876543211",
        "date": "10.09.2025",
        "comment": "Оставить у двери"
    }
]

class TestOrder:

    driver = None
    
    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Firefox()

    @allure.step("Открываем страницу Яндекс Самокат")
    def open_page(self):
        self.driver.get(URL)

    @allure.step ("Заполнение формы заказа")
    def fill_order(self,page,data):
        page.fill_order_form(data)

    @allure.step("Проверяем успешное создание заказа")
    def check_success_message(self, page):
        assert page.is_success_message_visible(), "Сообщение об успешном заказе не отображается"
    
    
    @pytest.mark.parametrize("data, button_type", [
        (order_data[0], "top"),
        (order_data[1], "bottom"),
    ])
    @allure.title("Проверка оформления заказа через {button_type} кнопку")
    def test_order_flow(self, data, button_type):
        self.open_page()
        main_page = MainPage(self.driver)
        
        if button_type == "top":
            main_page.click_top_order()
        else:
            main_page.click_bottom_order()

        order_page = OrderPage(self.driver)
        self.fill_order(order_page, data)
        self.check_success_message(order_page)
        
    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
    