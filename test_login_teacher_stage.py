from selene import browser, have


def test_login_teacher_true(open_browser):
    # Ввод логина и пароля
    browser.element('[type=text]').type('misha-marinov@mail.ru')
    browser.element('[type=password]').type('testGYvbueca0lf6')

    # Нажатие на кнопку входа -> Аккаунт учителя
    browser.element('button.blue').click()
    browser.element('button:nth-child(1)').click()
    browser.should(have.url_containing('/cabinet/teacher/lessons/schdule'))