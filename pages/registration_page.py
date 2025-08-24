from selene import browser, have, command


class RegistrationPage:
    def open(self):
        browser.open('/automation-practice-form')
        return self

    def register(self, user):
        browser.element('#firstName').type(user.first_name)
        browser.element('#lastName').type(user.last_name)
        browser.element('#userEmail').type(user.email)

        browser.all('[for^=gender-radio]').element_by(have.text(user.gender)).click()
        browser.element('#userNumber').type(user.mobile)


        browser.driver.execute_script('document.querySelector("#fixedban")?.remove()')
        browser.driver.execute_script('document.querySelector("footer")?.remove()')

        browser.element('#submit').perform(command.js.scroll_into_view)
        browser.element('#submit').perform(command.js.click)

        return self

    def should_have_registered(self, user):

        rows = browser.all('.modal-content tr')

        rows.element_by(have.text('Student Name')).should(
            have.text(f'{user.first_name} {user.last_name}')
        )
        rows.element_by(have.text('Student Email')).should(
            have.text(user.email)
        )
        rows.element_by(have.text('Gender')).should(
            have.text(user.gender)
        )
        rows.element_by(have.text('Mobile')).should(
            have.text(user.mobile)
        )



        return self
