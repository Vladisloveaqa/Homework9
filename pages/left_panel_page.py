from selene import browser


class LeftPanelPage:
    def open_simple_registration_form(self):
        browser.open('/text-box')
        return self
