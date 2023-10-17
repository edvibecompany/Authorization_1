from selene import browser, have, be


def test_empty_email_field(open_login_page):
    # Ввод пароля
    browser.element('[type=password]').type('password')

    # Нажатие на кнопку входа
    browser.element('button.blue').click()

    # Проверка, что возникла ошибка
    browser.element('.tir-input:nth-child(1) .tir-control').should(have.css_class('is-error'))
    browser.element('.tir-input:nth-child(1) .tir-error').should(be.visible).should(
        have.exact_text('Введите электронную почту'))
