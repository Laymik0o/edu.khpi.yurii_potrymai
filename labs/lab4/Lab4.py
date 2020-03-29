import random
import os
import re


# Use 'data/myBook.txt' and 'data/colors.txt' as example for watch how works this app
def main():
    task_1()
    task_2()
    task_3()


def task_1():
    list1 = ["hello", "ola", "good morning", "hi"]
    list2 = ["my name Bob", "I have pineapple", "dog is cucumber", "sun"]
    list3 = ["my shine ass", "star wars", "Spain", "whater"]
    text = random.choice(list1) + " " + random.choice(list2) + " " + random.choice(list3)
    print("My random phrase: ", text)


def task_2():
    text_with_space = get_symbols_from_file_with_space()
    text_without_space = get_symbols_without_space(text_with_space)
    words = get_words(text_with_space)
    words_dict = get_words_and_their_count_dict(words)
    print("Count symbols without space: %d" % len(text_without_space))
    print("Count symbols with space: %d" % len(text_with_space))
    print("Count of words: %d" % len(words))
    print("Count of unique words: %d" % len(words_dict))
    print("The сount of unique words that occur once : %d" % get_count_of_unique_words_that_occur_once(words_dict))
    # If you want print all unique words then uncomment next code
    # print("All unique words:")
    # for word in words_dict:
    #      print(word.ljust(20), words_dict[word])
    # If you don't know "ljust" then see - https://www.w3schools.com/python/ref_string_ljust.asp


def task_3():
    text_with_space = get_symbols_from_file_with_space().lower()
    colors_root = ["красн", "син", "зел", "жел", "бел"]
    colors = ["красный", "синий", "зеленый", "желтый", "белый"]
    count_color = list()
    for x in colors_root:
        patern = "\\b{color}\w*".format(color=x)
        color = re.findall(patern, text_with_space)
        count_color.append(len(color))
    print(dict(zip(colors, count_color)))


def get_symbols_from_file_with_space():
    filename = input("Enter path to file: ")
    try:
        with open(filename, encoding="utf8") as file:
            text = file.read()
        return text
    except FileNotFoundError:
        print("File not found")


def get_symbols_without_space(text):
    text = text.replace("\n", "").replace(" ", "")
    return text


def get_words(text):
    text = text.replace(",", "").replace(".", "").replace("?", "").replace("!", "").replace("—", "").replace("-", "")
    text = text.replace(":", "").replace("«", "").replace("»", "")
    text = text.lower()
    words = text.split()
    words.sort()
    return words


#  A set of unique words + their number
def get_words_and_their_count_dict(words):
    words_dict = dict()
    for word in words:
        if word in words_dict:
            words_dict[word] = words_dict[word] + 1
        else:
            words_dict[word] = 1
    return words_dict


def get_count_of_unique_words_that_occur_once(words_dict):
    counter = 0
    for v in words_dict.values():
        if v == 1:
            counter += 1
    return counter


if __name__ == "__main__":
    main()
