class Book:
    _name = ""
    _author = ""
    _genre = ""
    _year = 0

    def __init__(self, name, author, genre, year):
        self._name = name
        self._author = author
        self._genre = genre
        self._year = year

    def get_name(self):
        return self._name

    def get_author(self):
        return self._author

    def get_genre(self):
        return self._genre

    def get_year(self):
        return self._year

    def __str__(self):
        book_as_string = "Name: {0}, Author: {1}, Genre: {2}, Year of publishing: {3}"
        return book_as_string.format(self._name,
                                   self._author,
                                   self._genre,
                                   self._year)
