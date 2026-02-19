def count_error_occurrences(filename):
    count = 0
    try:
        with open(filename, "r") as file:
            for line in file:
                count += line.count("ERROR")
        print(f'"ERROR" appeared {count} times.')
    except FileNotFoundError:
        print("Log file not found.")

count_error_occurrences("app.log")