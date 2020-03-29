class EngRusDictionary:
    __dictionary = {}

    def add_translation(self, eng_word, rus_translation):
        if eng_word in self.__dictionary:
            self.__dictionary[eng_word].append(rus_translation)
        else:
            self.__dictionary[eng_word] = [rus_translation]

    def print_dictionary(self):
        print("Dictionary:")
        for word in self.__dictionary:
            print(word, self.__dictionary[word])

    def get_translation(self, eng_word):
        return self.__dictionary[eng_word]


def demo():
    dictionary = EngRusDictionary()
    first_word = "Georgia"
    second_word = "Dictionary"
    dictionary.add_translation(first_word, "Грузия")
    dictionary.add_translation(first_word, "Джорджия (штат США)")
    dictionary.add_translation(second_word, "словарь")
    dictionary.print_dictionary()
    print("translations for word '%s'" % first_word)
    print(dictionary.get_translation(first_word))
    print("translations for word '%s'" % second_word)
    print(dictionary.get_translation(second_word))


if __name__ == "__main__":
    demo()
