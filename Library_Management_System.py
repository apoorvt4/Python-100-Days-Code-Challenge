class Library:
    books = ["Lord of the rings", "Games of thrones", "Harry potter", "Matrix", "Death Note"]
    number_of_books = int(input("Enter The Number of Books"))


    def books_in_library(self):
        print(f"Name of the books is {self.books}")

    def check(self):
        if(self.number_of_books == len(self.books)):
            print(f"Number of available books are {self.number_of_books}")
        else:
            print(f"Sorry Number Of available are not there!!\n only {self.number_of_books} Left! ")
    

a = Library()
a.books_in_library()
a.check()
