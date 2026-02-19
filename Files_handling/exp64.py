import csv

books = [
    {"Title": "Harry potter", "Author": "J K Rowling", "Price": 45},
    {"Title": "Romeo Juliet", "Author": "Williams Shakespeare", "Price": 60},
    {"Title": "White Nights", "Author": "Fyodor dostoevsky", "Price": 80}
]

def write_books_to_csv(filename, books_list):
    try:
        with open(filename, "w", newline="") as file:
            fieldnames = books_list[0].keys()
            writer = csv.DictWriter(file, fieldnames=fieldnames)

            writer.writeheader()
            writer.writerows(books_list)

        print("Books written to CSV successfully.")
    except Exception as e:
        print("Error writing to CSV:", e)

write_books_to_csv("books.csv", books)