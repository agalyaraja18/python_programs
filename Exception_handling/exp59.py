import json

def read_json_file(filename):
    try:
        with open(filename, "r") as file:
            data = json.load(file)
            print("JSON Data:", data)
    except FileNotFoundError:
        print("Error: File not found.")
    except json.JSONDecodeError:
        print("Error: Invalid JSON format.")

read_json_file("data.json")