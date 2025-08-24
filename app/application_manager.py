from pages.registration_page import RegistrationPage


class ApplicationManager:
    def __init__(self):
        self.registration = RegistrationPage()
        # потом можно добавить и другие PageObject (например LeftPanel)

app = ApplicationManager()
