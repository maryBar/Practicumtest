from selenium.webdriver.common.by import By


class CalculatorPageLocators:
    ENTRY_FIELD = (By.CSS_SELECTOR, "entry field")
    BUTTON_ZERO = (By.XPATH, "//*[@role='button' and text() = '0']")
    BUTTON_EQUAL = (By.XPATH, "//*[@role='button' and text() = '=']")
    BUTTON_ONE = (By.XPATH, "//*[@role='button' and text() = '1']")
    BUTTON_TWO = (By.XPATH, "//*[@role='button' and text() = '2']")
    BUTTON_THREE = (By.XPATH, "//*[@role='button' and text() = '3']")
    BUTTON_FOUR = (By.XPATH, "//*[@role='button' and text() = '4']")
    BUTTON_FIVE = (By.XPATH, "//*[@role='button' and text() = '5']")
    BUTTON_SIX = (By.XPATH, "//*[@role='button' and text() = '6']")
    BUTTON_PLUS = (By.XPATH, "//*[@role='button' and text() = '+']")
    BUTTON_MINUS = (By.XPATH, "//*[@role='button' and text() = '−']")
    BUTTON_MULTIPLY = (By.XPATH, "//*[@role='button' and text() = '×']")
    BUTTON_DIVIDE = (By.XPATH, "//*[@role='button' and text() = '÷']")
    BUTTON_LEFT_PARENTHESIS = (By.XPATH, "//*[@role='button' and text() = '(']")
    BUTTON_RIGHT_PARENTHESIS = (By.XPATH, "//*[@role='button' and text() = ')']")
    BUTTON_SIN = (By.XPATH, "//*[@role='button' and text() = 'sin']")
    FORMULA_FIELD = (By.XPATH, "//span[@id='cwos']/../../../preceding-sibling::div//span")
    RESULT_STRING = (By.XPATH, "//*[@id='cwos']")


class MainPageLocators:
    SEARCH_FIELD = (By.CSS_SELECTOR, "[name='q']")
    SEARCH_BUTTON = (By.CSS_SELECTOR, "[name='btnK']")