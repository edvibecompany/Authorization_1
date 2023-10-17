from selene import browser, have, be


def test_login_student_true(open_login_page):
    # Ввод логина и пароля
    browser.element('[type=text]').type('sss@dsd.csd')
    browser.element('[type=password]').type('testGYvbueca0lf6')

    # Нажатие на кнопку входа -> Аккаунт ученика
    browser.element('button.blue').click()
    browser.wait_until(browser.element('.blue').should(be.visible))
    browser.element('.blue').click()
    browser.should(have.url_containing('/cabinet/student/lessons'))