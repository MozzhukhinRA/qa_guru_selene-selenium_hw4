import pytest
from selene import browser, have

browser.config.base_url = 'https://todomvc.com/examples/'

@pytest.mark.parametrize(
    'relative_url',
    ['preact/dist/', 'vue/dist/#/'], ids=["preact", "vue"]
)

def test_form_frameworks(relative_url):
    browser.open(relative_url)

    browser.element('.new-todo').type('My First Task').press_enter()

    browser.all('.todo-list li').should(have.exact_texts('My First Task'))