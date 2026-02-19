def check_age(age):
    if age < 18:
        raise ValueError("Age must be 18 or older.")
    return "Access granted"

try:
    print(check_age(16))
except ValueError as e:
    print("Error:", e)