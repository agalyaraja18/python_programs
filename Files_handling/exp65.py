import csv

def print_items_above_50(filename):
    try:
        with open(filename, "r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                if float(row["Price"]) > 50:
                    print(f"Author: {row['Author']}")
    except FileNotFoundError:
        print("CSV file not found.")
    except ValueError:
        print("Invalid data in CSV file.")

print_items_above_50("books.csv")