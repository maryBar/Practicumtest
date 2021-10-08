import allure

from locators.locators import MainPageLocators
from pages.base_page import BasePage


class MainPage(BasePage):
    def __init__(self, browser, url, timeout=10):
        super().__init__(browser, url, timeout)

    def entering_word_into_search_bar(self, value):
        search_field = self.browser.find_element(*MainPageLocators.SEARCH_FIELD)
        with allure.step(f"В поисковой строке ввести {value}"):
            search_field.send_keys(value)

    @allure.step("Нажать кнопку поиска")
    def click_search_button(self):
        search_button = self.browser.find_element(*MainPageLocators.SEARCH_BUTTON)
        search_button.click()
