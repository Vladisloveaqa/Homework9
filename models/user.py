from dataclasses import dataclass


@dataclass
class User:
    def __init__(self, first_name, last_name, email, gender, mobile, birth_date=None):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.gender = gender
        self.mobile = mobile
        self.birth_date = birth_date