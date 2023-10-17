import pytest
from selene import browser


@pytest.fixture()
def open_login_page():
    browser.open('https://stage.progressme.ru/')
    browser.element('.gray .button-content').click()
