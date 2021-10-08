import allure

from locators.locators import CalculatorPageLocators
from pages.base_page import BasePage


class CalculatorPage(BasePage):

    def __init__(self, browser, url=None, timeout=10):
        super().__init__(browser, url, timeout)

    @allure.step("Нажать левую скобку")
    def click_button_left_parenthesis(self):
        button_left_parenthesis = self.browser.find_element(*CalculatorPageLocators.BUTTON_LEFT_PARENTHESIS)
        button_left_parenthesis.click()

    @allure.step("Нажатие правую скобку")
    def click_button_right_parenthesis(self):
        button_right_parenthesis = self.browser.find_element(*CalculatorPageLocators.BUTTON_RIGHT_PARENTHESIS)
        button_right_parenthesis.click()

    @allure.step("Нажать кнопку плюс")
    def click_button_plus(self):
        button_plus = self.browser.find_element(*CalculatorPageLocators.BUTTON_PLUS)
        button_plus.click()

    @allure.step("Нажать кнопку минус")
    def click_button_minus(self):
        button_minus = self.browser.find_element(*CalculatorPageLocators.BUTTON_MINUS)
        button_minus.click()

    @allure.step("Нажать кнопку умножить")
    def click_button_multiply(self):
        button_multiply = self.browser.find_element(*CalculatorPageLocators.BUTTON_MULTIPLY)
        button_multiply.click()

    @allure.step("Нажать кнопку разделить")
    def click_button_divide(self):
        button_divide = self.browser.find_element(*CalculatorPageLocators.BUTTON_DIVIDE)
        button_divide.click()

    @allure.step("Нажать кнопку равно")
    def click_button_equal(self):
        button_equal = self.browser.find_element(*CalculatorPageLocators.BUTTON_EQUAL)
        button_equal.click()

    @allure.step("Нажать кнопку ноль")
    def click_button_zero(self):
        button_zero = self.browser.find_element(*CalculatorPageLocators.BUTTON_ZERO)
        button_zero.click()

    @allure.step("Нажать кнопку один")
    def click_button_one(self):
        button_one = self.browser.find_element(*CalculatorPageLocators.BUTTON_ONE)
        button_one.click()

    @allure.step("Нажать кнопку два")
    def click_button_two(self):
        button_two = self.browser.find_element(*CalculatorPageLocators.BUTTON_TWO)
        button_two.click()

    @allure.step("Нажать кнопку три")
    def click_button_three(self):
        button_three = self.browser.find_element(*CalculatorPageLocators.BUTTON_THREE)
        button_three.click()

    @allure.step("Нажать кнопку четыре")
    def click_button_four(self):
        button_four = self.browser.find_element(*CalculatorPageLocators.BUTTON_FOUR)
        button_four.click()

    @allure.step("Нажать кнопку пять")
    def click_button_five(self):
        button_five = self.browser.find_element(*CalculatorPageLocators.BUTTON_FIVE)
        button_five.click()

    @allure.step("Нажать кнопку шесть")
    def click_button_six(self):
        button_six = self.browser.find_element(*CalculatorPageLocators.BUTTON_SIX)
        button_six.click()

    @allure.step("Нажать кнопку sin")
    def click_button_sin(self):
        button_sin = self.browser.find_element(*CalculatorPageLocators.BUTTON_SIN)
        button_sin.click()

    def should_be_entered_formula(self, value):
        entered_formula = self.browser.find_element(*CalculatorPageLocators.FORMULA_FIELD).text
        with allure.step(f"В строке памяти отображается ранее введенная формула {value}"):
            assert entered_formula in value, "The previously entered formula"

    def should_be_answer_in_result_line(self, value):
        result_line = self.browser.find_element(*CalculatorPageLocators.RESULT_STRING).text
        with allure.step(f"В строке результата отображается {value}"):
            assert result_line == value, "The answer doesn't match"
