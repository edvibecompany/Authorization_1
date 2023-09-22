from selene import browser, be


def test_login_false(open_browser):
    # Ввод логина и невалидного пароля
    browser.element('[type=text]').type('misha-marinov@mail.ru')
    browser.element('[type=password]').type('testGYvbueca0lf')

    # Нажатие на кнпоку войти
    browser.element('button.blue').click()
    browser.element('.tir-error').should(be.visible)