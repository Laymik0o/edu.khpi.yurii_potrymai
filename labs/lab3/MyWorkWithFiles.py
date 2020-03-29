import csv
import os


def choice_option(choice):
    if choice == 1:
        choice = input("Choice group -> ")
        path = "data/{group}.csv".format(group=choice)
        print_all_from_file(path)
    elif choice == 2:
        choice = input("Choice group -> ")
        path = "data/{group}.csv".format(group=choice)
        print("Enter new record only as example -> '{Name} {Rating}; {Name2} {Rating2}'")
        users = input("Enter new records (Name Rating; Name Rating) -> ")
        append_records_to_file(path, users)
    elif choice == 3:
        choice = input("Choice group -> ")
        path = "data/{group}.csv".format(group=choice)
        users = input("Enter new records (Name Rating; Name Rating) -> ")
        write_new_records_to_file(path, users)
    elif choice == 4:
        choice = input("Choice group -> ")
        path = "data/{group}.csv".format(group=choice)
        user = input("Choice index of student -> ")
        search_and_print_by_index(path, user)
    elif choice == 5:
        choice = input("Choice group -> ")
        path = "data/{group}.csv".format(group=choice)
        sort_and_print_by_rating(path)
    elif choice == 6:
        choice = input("Choice directory -> ")
        search_csv_files_at_directory(choice)
    else:
        print("Bad choice")


def search_csv_files_at_directory(directory):
    try:
        files = os.listdir(directory)
        csv_files = filter(lambda x: x.endswith(".csv"), files)
        list_files = list(csv_files)
        if len(list_files) == 0:
            print("There aren't csv files")
        else:
            for f in list_files:
                print(f)
    except FileNotFoundError:
        print("File not found")


def sort_and_print_by_rating(file_name):
    try:
        with open(file_name, "r", newline="", encoding="utf-8") as file:
            reader = list(csv.reader(file))
            reader = list(filter(None, reader))  # Delete empty fields
            reader.sort(key=lambda i: i[1], reverse=True)
            for row in reader:
                print(row[0], " - ", row[1])
    except FileNotFoundError:
        print("File not found")


def search_and_print_by_index(file_name, index):
    try:
        with open(file_name, "r", newline="", encoding="utf-8") as file:
            line = file.readlines()[int(index)]
            print(line)
    except FileNotFoundError:
        print("File not found")
    except IndexError:
        print("Invalid index")


def write_new_records_to_file(file_name, users_to_write):
    users = users_to_write.split('; ')
    count_users = len(users)
    new_users = []
    for i in range(count_users):
        user = users[i].split(' ')
        new_users.append(user)
    with open(file_name, "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerows(new_users)


def append_records_to_file(file_name, users_to_write):
    users = users_to_write.split('; ')
    count_users = len(users)
    new_users = []
    for i in range(count_users):
        user = users[i].split(' ')
        new_users.append(user)
    with open(file_name, "a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerows(new_users)


def print_all_from_file(file_name):
    try:
        with open(file_name, "r", newline="", encoding="utf-8") as file:
            reader = csv.reader(file)
            for row in reader:
                print(row[0], " - ", row[1])
    except FileNotFoundError:
        print("File not found")
