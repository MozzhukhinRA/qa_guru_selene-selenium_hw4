from selene import browser, have


def test_required_form():
    browser.element('.text-center').should(have.exact_text('Practice Form'))

def test_personal_data():
    browser.element('#firstName').type('Ivan')
    browser.element('#lastName').type('Ivanov')

def test_mail_form():
    browser.element('#userEmail').type('qwerty@mail.ru')

def test_gender_checkbox():
    browser.element('.custom-control-input').should(have.value('Male'))
    browser.element('#gender-radio-1').click()
