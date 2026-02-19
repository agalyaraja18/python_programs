from abc import ABC, abstractmethod

class FileHandler(ABC):
    @abstractmethod
    def read(self, filename):
        pass
    @abstractmethod
    def write(self, filename, data):
        pass

class TextFileHandler(FileHandler):
    def read(self, filename):
        with open(filename, 'r') as file:
            content = file.read()
        return content
    def write(self, filename, data):
        with open(filename, 'w') as file:
            file.write(data)
        print("Text data written successfully.")

class CSVFileHandler(FileHandler):
    def read(self, filename):
        with open(filename, 'r') as file:
            content = file.readlines()
        return [line.strip().split(",") for line in content]
    def write(self, filename, data):
        with open(filename, 'w') as file:
            for row in data:
                file.write(",".join(row) + "\n")
        print("CSV data written successfully.")

text_handler = TextFileHandler()
text_handler.write("sample.txt", "Hello World")
print(text_handler.read("sample.txt"))
print()
csv_handler = CSVFileHandler()
csv_handler.write("sample.csv", [["Name", "Age"], ["Agalya", "22"]])
print(csv_handler.read("sample.csv"))