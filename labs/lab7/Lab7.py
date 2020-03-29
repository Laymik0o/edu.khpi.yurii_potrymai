from matplotlib import pylab
from numpy import *
import matplotlib.pyplot as plt
import re


# Use data/myBook.txt or data/sentences.txt for test this app
def main():
    task_1()
    task_2()
    task_3()


def task_1():
    t = linspace(0, 10, 50)
    y = t ** sin(10 * t)
    plt.plot(t, y, "r--", label="t^sin(10*t)")
    plt.savefig("data/plot_task_1.png", dpi=400)
    plt.xlabel("t")
    plt.ylabel("y")
    plt.title("My first normal plot")
    plt.legend()
    plt.show()


def task_2():
    symbols_dict = get_symbols_dict(get_symbols(get_text()))
    x_data = symbols_dict.keys()
    y_data = symbols_dict.values()
    pylab.bar(x_data, y_data)
    pylab.savefig("data/plot_task_2.png", dpi=400)
    pylab.show()


def task_3():
    sentences_dict = count_of_each_sentences(get_text())
    x_data = sentences_dict.keys()
    y_data = sentences_dict.values()
    pylab.bar(x_data, y_data)
    pylab.savefig("data/plot_task_3.png", dpi=400)
    pylab.show()


def get_text():
    filename = input("Enter path to file: ")
    try:
        with open(filename, encoding="utf8") as file:
            text = file.read()
        return text
    except FileNotFoundError:
        print("File not found")


def get_symbols(text):
    text = text.replace("\n", "").replace(" ", "").replace(",", "").replace(".", "").replace("?", "")
    text = text.replace("!", "").replace("—", "").replace("-", "").replace(":", "").replace("«", "").replace("»", "")
    text = text.lower()
    text = list(text)
    text.sort()
    return text


#  A set of unique symbols + their count
def get_symbols_dict(symbols):
    symbols_dict = dict()
    for symbol in symbols:
        if symbol in symbols_dict:
            symbols_dict[symbol] = symbols_dict[symbol] + 1
        else:
            symbols_dict[symbol] = 1
    return symbols_dict


def count_of_each_sentences(text):
    text = text.replace("\n", " ").replace("—", "") + " "  # add space at end of text for correct work regex (line 72)
    list_delimiters = ["!", "?", ".{3}", ".{1}"]
    types_sentence = ["Восклицательное", "Вопросительное", "Три точки", "Обычное"]
    count_sentences = list()
    for x in list_delimiters:
        patern = "\w[\w\,\s]*\{delimiter}\s".format(delimiter=x)
        sentences = re.findall(patern, text)
        count_sentences.append(len(sentences))
    return dict(zip(types_sentence, count_sentences))


if __name__ == "__main__":
    main()
