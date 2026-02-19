from abc import ABC, abstractmethod
import re

class Validator(ABC):
    @abstractmethod
    def validate(self, data):
        pass

class EmailValidator(Validator):
    def validate(self, data):
        pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
        if re.match(pattern, data):
            return "Valid Email"
        return "Invalid Email"

class PasswordValidator(Validator):
    def validate(self, data):
        if (len(data) >= 8 and
            re.search(r'[A-Z]', data) and
            re.search(r'[a-z]', data) and
            re.search(r'\d', data) and
            re.search(r'[!@#$%^&*(),.?":{}|<>]', data)):
            return "Valid Password"
        return "Invalid Password"

email_validator = EmailValidator()
password_validator = PasswordValidator()
print(email_validator.validate("test@example.com"))
print(email_validator.validate("invalid-email"))
print(password_validator.validate("StrongPass1!"))
print(password_validator.validate("weak"))