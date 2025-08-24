from app.application_manager import ApplicationManager


def test_simple_registration():
    app = ApplicationManager()

    app.left_panel.open_simple_registration_form()

