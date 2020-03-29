import random

from labs.lab5.task4.CardDeck import CardDeck


def demo():
    card_deck = CardDeck()
    card_deck.print_deck()
    card_deck.shuffle_deck()
    print("Shuffled deck:")
    card_deck.print_deck()
    print("Get one card:")
    print(card_deck.get_card())
    print("Get six cards:")
    card_deck.get_six_cards()
    print("Print card py it's position:")
    position = random.randint(1, 52)
    print("Generated position:", position)
    card_deck.print_card(position)


if __name__ == "__main__":
    demo()
