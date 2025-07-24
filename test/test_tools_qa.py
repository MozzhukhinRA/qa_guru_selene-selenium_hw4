import os
from selene import browser, be, have


def test_requirement_form():

    uploading = os.path.join(os.path.dirname(__file__), 'upload.txt')

    # заполнение личных данных
    browser.element('#firstName').should(be.visible).type('Ivan')
    browser.element('#lastName').should(be.visible).type('Ivanov')
    # заполнение эл почты
    browser.element('#userEmail').should(be.visible).type('Ivanov@mail.ru')
    # выбор чекбокса Female
    browser.all('.custom-control-input').element_by(have.value('Other')).element('..').click()
    # ввод номера телефона
    browser.element('#userNumber').should(be.visible).type('9871234567')
    # ввод даты
    browser.element('#dateOfBirthInput').should(be.visible).click()
    browser.element('.react-datepicker__month-select').type('April')
    browser.element('.react-datepicker__year-select').type('2000')
    browser.element('.react-datepicker__day--015').click()
    # заполнение области subject
    browser.element('#subjectsInput').type('Arts').press_enter().type('Accounting').press_enter()
    # выбор чекбокса Hobbies
    browser.all('.custom-control').element_by(have.exact_text('Sports')).click()
    # загрузка файла
    browser.element('.form-control-file').with_(timeout=5).should(be.visible).send_keys(uploading)
    # заполнение Current Address
    browser.element('#currentAddress').should(be.visible).type('publish')
    # выбор штата
    browser.element('#state').click()
    browser.element('#react-select-3-option-1').click()
    # выбор города
    browser.element('#city').click()
    browser.element('#react-select-4-option-2').click()
    # вызов submit
    browser.element('#submit').press_enter()
    # проверка формы
    browser.element('#example-modal-sizes-title-lg').should(have.text('Thanks for submitting the form'))
    browser.all('.table-responsive td:nth-child(2)').should(have.texts(
        'Ivan Ivanov',
        'Ivanov@mail.ru',
        'Other',
        '9871234567',
        '15 April,2000',
        'Arts, Accounting',
        'Sports',
        'upload.txt',
        'publish',
        'Uttar Pradesh Merrut'
    ))
