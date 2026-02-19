import re

def check_date_prefix(text):
    pattern = r'^\d{4}-\d{2}-\d{2}'
    if re.match(pattern, text):
        print("String starts with a valid YYYY-MM-DD date format.")
    else:
        print("String does NOT start with a valid date format.")

check_date_prefix("2025-11-30 Report Generated")