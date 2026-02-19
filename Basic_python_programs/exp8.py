correct_password = input("Enter your password: ")
max_attempts = int(input("Enter the maximum number of attempts: "))
attempts = 0
while attempts < max_attempts:
    user_input = input("Enter password: ")
    if user_input == correct_password:
        print("Access Granted")
        break
    attempts += 1
    print(f"Incorrect password. Attempts left: {max_attempts - attempts}")
print("Access Denied. Too many failed attempts.")