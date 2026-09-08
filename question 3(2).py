class Book :
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

    def display_details(self):
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Price: ${self.price}\n")

book1 = Book("Things Fall Apart", "Chinua Achebe", 15.00)
book2 = Book("The Alchemist", "Paulo Coelho", 20.00)

print('Book Details:')
book1.display_details()
book2.display_details()