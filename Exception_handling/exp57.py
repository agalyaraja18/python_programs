import logging

logging.basicConfig(
    filename="error_log.txt",
    level=logging.ERROR,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

class InvalidEmailError(Exception):
    pass

def validate_email(email):
    if "@" not in email:
        raise InvalidEmailError("Email must contain '@' symbol.")
    return True

try:
    validate_email("invalidemail.com")
except InvalidEmailError as e:
    logging.error("InvalidEmailError occurred", exc_info=True)