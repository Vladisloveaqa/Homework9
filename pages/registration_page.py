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


        browser.execute_script('document.querySelector("#fixedban")?.remove()')
        browser.execute_script('document.querySelector("footer")?.remove()')


        browser.element('#submit').perform(command.js.scroll_into_view)
        browser.element('#submit').perform(command.js.click)

        return self
    def should_have_registered(self, user):
        browser.element('.modal-content').should(
            have.texts(
                f'{user.first_name} {user.last_name}',
                user.email,
                user.mobile
            )
        )
        return self