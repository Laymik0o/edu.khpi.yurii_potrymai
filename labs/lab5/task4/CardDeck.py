from enum import Enum
import random


class Card:
    def __init__(self, number, suit):
        self.number = number
        self.suit = suit

    def __str__(self):
        card_as_string = "Number: {0} Suite: {1}"
        return card_as_string.format(self.number, self.suit)

    def __eq__(self, o: object) -> bool:
        return (isinstance(o, Card)
                and o.suit == self.suit
                and o.number == self.number)


class CardDeck:
    __deck = []

    def __init__(self):
        while len(self.__deck) != 52:
            number = random.randint(2, 14)
            suite = self.__suites[random.randint(1, 4)]
            card = Card(number, suite)
            try:
                self.__deck.index(card)
            except ValueError:
                self.__deck.append(card)

    def get_card(self):
        return random.choice(self.__deck)

    def get_six_cards(self):
        return random.sample(self.__deck, 6)

    def shuffle_deck(self):
        random.shuffle(self.__deck)

    def print_card(self, position):
        print("Card: ", self.__deck[position - 1])

    def print_deck(self):
        print("Card deck:\n")
        for card in self.__deck:
            print(card, "\n")

    __suites = {
        1: "clubs",
        2: "diamonds",
        3: "hearts",
        4: "spades"
    }
