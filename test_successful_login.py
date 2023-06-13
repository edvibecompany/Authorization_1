from selene import browser, have, be

def test_login_true():
    browser.open('https://edvibe.com/Account/Login')
    browser.element('.form-input [name=Email]').type('misha-marinov@mail.ru')
    browser.element('.form-input [name=Password]').type('liveUT00mPE8CB7Z').press_enter()
    browser.wait_until(browser.element('div.auth-form.auth-container > form > button:nth-child(4)').should(be.visible))
    browser.element('div.auth-form.auth-container > form > button:nth-child(4)').click()
    browser.should(have.url_containing('/TeacherAccount/?Login=true'))