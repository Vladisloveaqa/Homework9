from models.user import User
from pages.registration_page import RegistrationPage


def test_student_registration():
    student = User(
        first_name='Yasha',
        last_name='Kramarenko',
        email='yashaka@gmail.com',
        gender='Male',
        phone='1234567890'
    )

    registration_page = RegistrationPage()
    registration_page.open().register(student).should_have_registered(student)
