class Library:
    def __init__(self):
        self._book_list=[]
    
    def entry_book(self, book):
        self._book_list.append(book)
    
    def view_book(self):
        if self._book_list:
            for book in self._book_list:
                book.view_book_info()
    
    def find_book(self, bool_id):
        for book in self._book_list:
            if book.get_book_id() == bool_id:
                return book
        return None

class Book:
    def __init__(self, book_id, tittle, author, availablity = True):
        self.__book_id = book_id
        self.__tittle = tittle
        self.__author = author
        self.__availablity = availablity

    def get_book_id(self):
        return self.__book_id
    
    def borrow_book(self):
        if self.__availablity:
            self.__availablity = False
            print(f'Book {self.__tittle} borrow successfully.\n')
        else:
            print(f'Book {self.__tittle} is already borrowed.\n')

    def return_book(self):
        if not self.__availablity:
            self.__availablity = True
            print(f'Book {self.__tittle} returned successfully.\n')
        else:
            print(f'Book {self.__tittle} was not borrowed.\n') 
    
    def view_book_info(self):
        availablity_status = 'Available' if self.__availablity else 'Not Availablity'
        print(f'Book Id: {self.__book_id} Tittle: {self.__tittle} Author: {self.__author} Status: {availablity_status}')


def manu_system():
    library = Library()

    book1 = Book('101', 'Python Programming', 'Guido van Rossum')
    book2 = Book('102', 'Clean Code', 'Robert C.Martin')
    book3 = Book('103', 'The Paramatic Programer', 'Andrew Hunt')
    book4 = Book('104', 'Badhon Hara', 'Kazi Nazrul Islam')
    book5 = Book('105', 'Shiuli mala', 'Kazi Nazrul Islam')
    book6 = Book('106', 'Hajar Bochor Dhore', 'Zahir Raihan')
    book7 = Book('107', 'Padma Nodir Majhi', 'Manik Bandopadhyay')

    library.entry_book(book1)
    library.entry_book(book2)
    library.entry_book(book3)
    library.entry_book(book4)
    library.entry_book(book5)
    library.entry_book(book6)
    library.entry_book(book7)

    while True:
        print('\n')
        print('------ Library Menu---------\n')
        print('1. View All Books')
        print('2. Borrow Book')
        print('3. Return Book')
        print('4. Exit')
        print('\n')
        choice = input("Enter your choice: ")
        if choice == '1':
            library.view_book()
        elif choice == '2':
            book_id = input("Enter the book id to borrow : ")
            book = library.find_book(book_id)
            if book:
                book. borrow_book()
            else:
                print("Error, Invalid book id\n")
        elif choice == '3':
            book_id = input("Enter the book id to return: ")
            book = library.find_book(book_id)
            if book:
                book.return_book()
            else:
                print("Error, Invalid book id\n")
        elif choice == '4':
            print('Exiting library system\n')
            break
        else:
            print('Invalid choice, Please try again\n')

manu_system()

                
    
