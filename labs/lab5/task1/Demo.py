from labs.lab5.task1.HomeLib import HomeLib


def start():
    library = HomeLib()
    library.add_book()
    library.add_book()
    library.print_library()
    print(library.get_book())
    print(library.get_book_by_number())
    library.delete_book()
    library.print_library()


if __name__ == "__main__":
    start()
