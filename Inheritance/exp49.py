class Writer:
    def write(self):
        print("Writing content...")

class Reader:
    def read(self):
        print("Reading content...")

class Editor(Writer, Reader):
    def edit(self):
        print("Editing content...")

obj = Editor()
obj.write()
obj.read()
obj.edit()