import allure

from pages.calculator_page import CalculatorPage
from pages.main_page import MainPage


@allure.feature("Проверка работы Google калькулятора")
class TestCalculatorPage:
    google_url = "https://www.google.ru/"

    @allure.story("Проверка операций с целыми числами")
    def test_checking_integer_operations(self, browser):
        main_page = MainPage(browser, TestCalculatorPage.google_url)
        calculator_page = CalculatorPage(browser)

        main_page.open()
        main_page.entering_word_into_search_bar("Калькулятор")
        main_page.click_search_button()

        calculator_page.click_button_left_parenthesis()
        calculator_page.click_button_one()
        calculator_page.click_button_plus()
        calculator_page.click_button_two()
        calculator_page.click_button_right_parenthesis()
        calculator_page.click_button_multiply()
        calculator_page.click_button_three()
        calculator_page.click_button_minus()
        calculator_page.click_button_four()
        calculator_page.click_button_zero()
        calculator_page.click_button_divide()
        calculator_page.click_button_five()
        calculator_page.click_button_equal()

        calculator_page.should_be_entered_formula("(1 + 2) × 3 - 40 ÷ 5 =")
        calculator_page.should_be_answer_in_result_line("1")

    @allure.story("Проверка деления на ноль")
    def test_division_by_zero_check(self, browser):
        main_page = MainPage(browser, TestCalculatorPage.google_url)
        calculator_page = CalculatorPage(browser)

        main_page.open()
        main_page.entering_word_into_search_bar("Калькулятор")
        main_page.click_search_button()

        calculator_page.click_button_six()
        calculator_page.click_button_divide()
        calculator_page.click_button_zero()
        calculator_page.click_button_equal()

        calculator_page.should_be_entered_formula("6 ÷ 0 =")
        calculator_page.should_be_answer_in_result_line("Infinity")

    @allure.story("Проверка ошибки при отсутствии значения")
    def test_error_check_if_missing_meaning(self, browser):
        main_page = MainPage(browser, TestCalculatorPage.google_url)
        calculator_page = CalculatorPage(browser)

        main_page.open()
        main_page.entering_word_into_search_bar("Калькулятор")
        main_page.click_search_button()

        calculator_page.click_button_sin()
        calculator_page.click_button_equal()
        calculator_page.should_be_entered_formula("sin() =")
        calculator_page.should_be_answer_in_result_line("Error")
