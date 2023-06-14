from selene import browser, have, be

def test_sections_check():
    browser.open('https://preview.edvibe.com/Account/Login')
    browser.element('.form-input [name=Email]').type('misha-marinov@mail.ru')
    browser.element('.form-input [name=Password]').type('liveUT00mPE8CB7Z').press_enter()
    browser.wait_until(browser.element('div.auth-form.auth-container > form > button:nth-child(4)').should(be.visible))
    browser.element('div.auth-form.auth-container > form > button:nth-child(4)').click()
    browser.wait_until(have.url('https://edvibe.com/TeacherAccount/lessons'))
    browser.element('div.tabs > div:nth-child(2)').click()
    browser.element('div.row.title-page-class.no-gutters > div').should(have.text('Обучение'))
    browser.element('div.tabs > div:nth-child(3)').click()
    browser.element('.materials-title').should(have.text('Материалы'))
    browser.element('div.tabs > div:nth-child(4)').click()
    browser.element('.head').should(have.text('Настройки'))
    browser.element('div.tabs > div:nth-child(1)').click()
    browser.element('.text-translate').should(have.text('Расписание уроков'))