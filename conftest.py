import pytest
from selenium import webdriver


@pytest.fixture(scope="function")
def browser():
    browser = webdriver.Chrome("webdrivers//chromedriver.exe")
    yield browser

    browser.quit()
