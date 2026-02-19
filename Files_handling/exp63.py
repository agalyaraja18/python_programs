import json

def print_json_key(filename, key):
    try:
        with open(filename, "r") as file:
            data = json.load(file)
            if key in data:
                print(f"Value of '{key}': {data[key]}")
            else:
                print("Key not found in JSON file.")
    except FileNotFoundError:
        print("JSON file not found.")
    except json.JSONDecodeError:
        print("Invalid JSON format.")

print_json_key("data.json", "name")