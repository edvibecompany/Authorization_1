from selene import browser, have, be


def test_invalid_email(open_login_page):
    # Ввод логина и пароля
    browser.element('[type=text]').type('42@mail.ru')
    browser.element('[type=password]').type('testGYvbueca0lf6')

    # Нажатие на кнопку входа
    browser.element('button.blue').click()

    # Проверка, что возникла ошибка
    browser.element('.tir-error').should(be.visible).should(have.exact_text('Пользователь не найден'))
