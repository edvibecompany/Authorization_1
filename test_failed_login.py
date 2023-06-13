from selene import browser, have

def test_login_false():
    browser.open('https://edvibe.com/Account/Login')
    browser.element('.form-input [name=Email]').type('misha-marinov@mail.ru')
    browser.element('.form-input [name=Password]').type('password')
    browser.element('div.auth-form.auth-container > form > button').click()
    browser.element('.error-text').should(have.text('Login and password are wrong.'))