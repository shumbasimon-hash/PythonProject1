from abc import ABC, abstractmethod


class FileHandler(ABC):

    @abstractmethod
    def read(self):
        pass

    @abstractmethod
    def write(self, data):
        pass


class TextFileHandler(FileHandler):

    def read(self):
        print("Reading data from a text file.")

    def write(self, data):
        print("Writing text data:", data)


class BinaryFileHandler(FileHandler):

    def read(self):
        print("Reading binary data from a binary file.")

    def write(self, data):
        print("Writing binary data:", data)


# Create objects
text_file = TextFileHandler()
binary_file = BinaryFileHandler()

# Use the methods
text_file.read()
text_file.write("Hello Python")

binary_file.read()
binary_file.write(b"101010")