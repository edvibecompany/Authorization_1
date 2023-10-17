from selene import browser, have, be


def test_incorrect_format_email(open_login_page):
    # Ввод логина и пароля
    browser.element('[type=text]').type('12345*#fjdf')
    browser.element('[type=password]').type('testGYvbueca0lf6')

    # Нажатие на кнопку входа
    browser.element('button.blue').click()

    # Проверка, что возникла ошибка
    browser.element('.tir-input:nth-child(1) .tir-control').should(have.css_class('is-error'))
    browser.element('.tir-input:nth-child(1) .tir-error').should(be.visible).should(
        have.exact_text('Пожалуйста, введите правильный адрес электронной почты'))
