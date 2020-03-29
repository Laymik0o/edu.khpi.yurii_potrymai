class StringExtender(str):
    def is_palindrome(self, s):
        return s.lower() == s[len(s)::-1].lower()

    def has_sequences(self, s):
        if len(s) > 3:
            for i in range(len(s) - 3):
                s2 = s[i:i + 3]
                if s.find(s2, i + 1, len(s)) != -1:
                    return True
        return False


def demo():
    string_ext = StringExtender()
    print(string_ext.is_palindrome("kazak"))
    print(string_ext.is_palindrome("notpalindrome"))
    print(string_ext.is_palindrome(""))
    print(string_ext.has_sequences("no sequences"))
    print(string_ext.has_sequences("hunt or be hunted"))


if __name__ == "__main__":
    demo()
