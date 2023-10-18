from selene import browser, have, be


def test_invalid_password(open_login_page):
    # Ввод логина и пароля
    browser.element('[type=text]').type('43@mail.ru')
    browser.element('[type=password]').type('password*123!')

    # Нажатие на кнопку входа
    browser.element('button.blue').click()

    # Проверка, что возникла ошибка
    browser.element('.tir-error').should(be.visible).should(have.exact_text('Пользователь не найден'))
