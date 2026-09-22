class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

    def display_details(self):
        print("Title:", self.title)
        print("Author:", self.author)
        print("Price:", self.price)
        print()


# Instantiate two book objects
book1 = Book("Python Programming", "John Smith", 25.50)
book2 = Book("Introduction to Programming", "Mary Jones", 30.00)

# Display book details
book1.display_details()
book2.display_details()