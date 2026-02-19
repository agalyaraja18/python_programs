import re

def extract_domain(email):
    pattern = r'@([\w.-]+)'
    match = re.search(pattern, email)
    if match:
        print("Domain:", match.group(1))
    else:
        print("Invalid email format")

email=input("Enter email: ")
extract_domain(email)