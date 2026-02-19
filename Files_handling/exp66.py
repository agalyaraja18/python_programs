def replace_word_in_file(filename, old_word, new_word):
    try:
        with open(filename, "r") as file:
            content = file.read()

        content = content.replace(old_word, new_word)

        with open(filename, "w") as file:
            file.write(content)

        print("Word replacement completed successfully.")
    except FileNotFoundError:
        print("File not found.")

replace_word_in_file("sample.txt", "Python", "Java")