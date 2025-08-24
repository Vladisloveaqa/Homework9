from selene import browser, have


class RegistrationPage:

    def open(self):
        browser.open('/automation-practice-form')
        return self

    def register(self, user):
        browser.element('#firstName').type(user.first_name)
        browser.element('#lastName').type(user.last_name)
        browser.element('#userEmail').type(user.email)
        browser.all('[name=gender]').element_by(have.value(user.gender)).element('..').click()
        browser.element('#userNumber').type(user.phone)
        browser.element('#submit').click()
        return self

    def should_have_registered(self, user):
        modal = browser.element('.modal-content')
        modal.should(have.text(f'{user.first_name} {user.last_name}'))
        modal.should(have.text(user.email))
        modal.should(have.text(user.gender))
        modal.should(have.text(user.phone))
        return self
