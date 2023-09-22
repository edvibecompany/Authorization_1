from selene import browser, have


def test_login_school_true(open_browser):
    # Ввод логина и пароля
    browser.element('[type=text]').type('43@mail.ru')
    browser.element('[type=password]').type('testGYvbueca0lf6')

    # Нажатие на кнопку входа -> Аккаунт школы
    browser.element('button.blue').click()
    browser.element('.user-role-list button:nth-child(2)').click()
    browser.should(have.url_containing('/cabinet/school/indicators'))