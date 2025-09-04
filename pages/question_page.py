import allure
from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class QuestionPage(BasePage):

    title_question = (By.XPATH, "//span[text()='Вопросы о важном']")
    section_question = (By.CLASS_NAME, "accordion")

    question_1 = (By.XPATH, "//div[@class='accordion__button' and text()='Сколько это стоит? И как оплатить?']")
    question_2 = (By.XPATH, "//div[@class='accordion__button' and text()='Хочу сразу несколько самокатов! Так можно?']")
    question_3 = (By.XPATH, "//div[@class='accordion__button' and text()='Как рассчитывается время аренды?']")
    question_4 = (By.XPATH, "//div[@class='accordion__button' and text()='Можно ли заказать самокат прямо на сегодня?']")
    question_5 = (By.XPATH, "//div[@class='accordion__button' and text()='Можно ли продлить заказ или вернуть самокат раньше?']")
    question_6 = (By.XPATH, "//div[@class='accordion__button' and text()='Вы привозите зарядку вместе с самокатом?']")
    question_7 = (By.XPATH, "//div[@class='accordion__button' and text()='Можно ли отменить заказ?']")
    question_8 = (By.XPATH, "//div[@class='accordion__button' and text()='Я жизу за МКАДом, привезёте?']")

    answer_1 = (By.XPATH, "//div[@id='accordion__panel-0']")
    answer_2 = (By.XPATH, "//div[@id='accordion__panel-1']")
    answer_3 = (By.XPATH, "//div[@id='accordion__panel-2']")
    answer_4 = (By.XPATH, "//div[@id='accordion__panel-3']")
    answer_5 = (By.XPATH, "//div[@id='accordion__panel-4']")
    answer_6 = (By.XPATH, "//div[@id='accordion__panel-5']")
    answer_7 = (By.XPATH, "//div[@id='accordion__panel-6']")
    answer_8 = (By.XPATH, "//div[@id='accordion__panel-7']")

    @allure.step("Кликаем по вопросу и проверяем отображение ответа")
    def click_question_and_check_answer(self, question_locator, answer_locator):
        self.scroll_into_view(question_locator)
        self.click(question_locator)
        return self.wait_for_element_visible(answer_locator).is_displayed()
