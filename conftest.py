import pytest
from selene import browser
from selenium import webdriver


@pytest.fixture(scope="function", autouse=True)
def browser_open():
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    options.add_argument('--disable-gpu')

    browser.config.window_weight = 1920
    browser.config.window_height = 1080
    browser.open('https://demoqa.com/automation-practice-form')

    yield
    browser.quit()

