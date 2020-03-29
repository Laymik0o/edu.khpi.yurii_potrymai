from labs.lab5.task1.model.Book import Book


class HomeLib:
    library = []

    def add_book(self):
        print("Adding a new book to library")
        name = input("Enter name of the book: ")
        author = input("Enter name of the author: ")
        genre = input("Enter book genre: ")
        year = int(input("Enter the year of publishing: "))
        new_book = Book(name, author, genre, year)
        self.library.append(new_book)

    def get_book(self):
        search = int(input("Choose parameter to search:\n"
                           "1 - Name\n"
                           "2 - Author\n"
                           "3 - Genre\n"
                           "4 - Year\n"))
        parameter = input("Enter parameter value to search: ")
        book = self._search(search, parameter)
        if isinstance(book, Book):
            return book

    def _search(self, search, parameter):
        book = None
        if search == 1:
            book = self._get_book_by_name(parameter)
        elif search == 2:
            book = self._get_book_by_author(parameter)
        elif search == 3:
            book = self._get_book_by_genre(parameter)
        elif search == 4:
            book = self._get_book_by_year(parameter)
        else:
            print("Wrong number")
        return book

    def _get_book_by_name(self, name):
        for book in self.library:
            if book.get_name() == name:
                return book
        print("Book not founded")

    def _get_book_by_author(self, author):
        for book in self.library:
            if book.get_author() == author:
                return book
        print("Book not founded")

    def _get_book_by_genre(self, genre):
        for book in self.library:
            if book.get_genre() == genre:
                return book
        print("Book not founded")

    def _get_book_by_year(self, year):
        for book in self.library:
            if book.get_year() == year:
                return book
        print("Book not founded")

    def get_book_by_number(self):
        number = int(input("Enter number of the book"))
        return self.library[number]

    def delete_book(self):
        print("Deleting book")
        book = self.get_book()
        if isinstance(book, Book):
            self.library.remove(book)
        else:
            print("Nothing found")

    def print_library(self):
        for book in self.library:
            print(book)
