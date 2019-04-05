from random import shuffle


class Deck():
    suits = ["♣", "♥", "♠", "♦"]

    cards = dict(
        ACE=11,
        TWO=2,
        THREE=3,
        FOUR=4,
        FIVE=5,
        SIX=6,
        SEVEN=7,
        EIGHT=8,
        NINE=9,
        TEN=10,
        JACK=10,
        QUEEN=10,
        KING=10)

    def __init__(self):
        self.__deck = []
        for suit in self.suits:
            for card in self.cards.items():
                self.__deck.append(Card(card[0], suit, card[1]))
        shuffle(self.__deck)

    def deal_card(self):
        top = self.__deck[0]
        self.__deck.remove(top)
        return top

    def get_initial_cards(self):
        initialCards = self.__deck[0: 2]
        for i in initialCards:
            self.__deck.remove(i)
        return initialCards

    @staticmethod
    def sum_points(cards):
        points = 0
        for card in cards:
            points += card.get_value()
        return points


class Card():
    def __init__(self, name, suit, value):
        self.__name = name
        self.__suit = suit
        self.__value = value

    def __str__(self):
        return self.__name + " of " + self.__suit

    def get_name(self):
        return self.__name

    def get_value(self):
        return self.__value

    def get_suit(self):
        return self.__suit
