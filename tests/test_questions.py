import allure
import pytest
from selenium import webdriver
from pages.question_page import QuestionPage

URL = "https://qa-scooter.praktikum-services.ru/"

class TestQuestions:

    driver = None
    
    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Firefox()

    @allure.step("Открываем страницу Яндекс Самокат")
    def open_page(self):
        self.driver.get(URL)
 

    @allure.step("Кликаем по вопросу и проверяем, что ответ отображается")
    def check_question(self, page, question_locator, answer_locator):
        assert page.click_question_and_check_answer(question_locator, answer_locator), "Ответ не отображается"

    @pytest.mark.parametrize("question_locator, answer_locator", [
        (QuestionPage.question_1, QuestionPage.answer_1),
        (QuestionPage.question_2, QuestionPage.answer_2),
        (QuestionPage.question_3, QuestionPage.answer_3),
        (QuestionPage.question_4, QuestionPage.answer_4),
        (QuestionPage.question_5, QuestionPage.answer_5),
        (QuestionPage.question_6, QuestionPage.answer_6),
        (QuestionPage.question_7, QuestionPage.answer_7),
        (QuestionPage.question_8, QuestionPage.answer_8),
    ])
    def test_question(self, question_locator, answer_locator):
        page = QuestionPage(self.driver)
        self.open_page()
        self.check_question(page, question_locator, answer_locator)

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
