# -*- coding: utf-8 -*-
''' 
    The BlackJack
'''
from random import randint
from time import sleep


class BlackJack():
    Suits = ["♣", "♥", "♠", "♦"]
    Cards = dict(
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
    possible_cards = list(Cards.keys())
    __count_reset = 0

    def __init__(self):

                #----Human----#
        self.actual_bet = 0
        for _ in range(5):
            try:
                if self.__count_reset == 0:
                    self.Actual_money = float(
                        input("How much money do you have?\n"))
                    self.initial_money = self.Actual_money
                None
            except:
                print("Please, use only numbers")
            else:
                self.Human_cards = [
                    [self.possible_cards[randint(0, 12)],
                     self.Suits[randint(0, 3)]],
                    [self.possible_cards[randint(0, 12)],
                     self.Suits[randint(0, 3)]]]
                self.Human_points = sum([self.Cards[i[0]]
                                         for i in self.Human_cards])
                #----Computer----#
                self.__Computer_cards = [
                    [self.possible_cards[randint(0, 12)],
                     self.Suits[randint(0, 3)]],
                    [self.possible_cards[randint(0, 12)],
                     self.Suits[randint(0, 3)]]]
                self.Visible_computer_cards = self.__Computer_cards[0]
                self.__Computer_points = sum([self.Cards[i[0]]
                                              for i in self.__Computer_cards])
                #----Start Game----#
                self.__count_reset = 1
                self.__check_ace()
                self.__check_bet()
                break

    def __str__(self):

        return "This awesome BlackJack game is created by Davichete, and it has been supervised by Bord"

    def __len__(self):

        return 1

    def __check_ace(self):
        if "ACE" in [i[0] for i in self.Human_cards]:
            if self.Human_points > 21:
                self.Human_points -= 10

    def __check_bet(self):

        print("Your actual money is " + str(self.Actual_money))
        for _ in range(5):
            try:
                self.actual_bet = int(input("What bet do you wanna make?\n"))
                break
            except:
                print("Please, use only numbers")

        for _ in range(5):
            if self.actual_bet > self.Actual_money:
                print("You cannot make a bet bigger than your actual money.\n")
                self.actual_bet = int(input("What bet do you wanna make?\n"))
            elif self.actual_bet == 0:
                print("The bet must be greater than 0.\n")
                self.actual_bet = int(input("What bet do you wanna make?\n"))
            else:
                self.__start_game()
                break

    def __start_game(self):

        print("The game has started, it is your turn.\n")
        sleep(2)
        print("Your cards are " +
              self.Human_cards[0][0] + " of " + self.Human_cards[0][1] +
              " and " + self.Human_cards[1][0] + " of " + self.Human_cards[1][1] + ".\n")
        sleep(2)
        print("The first card of the bank is " +
              self.Visible_computer_cards[0] + " of " + self.Visible_computer_cards[1] + "\n")
        self.__human_win_lose_condition()
        self.__human_turn()

    __counter_computer = 0

    def __computer_turn(self):

        if self.__counter_computer == 0:
            print("Now it is the bank turn.")
            self.__counter_computer = 1
        self.__update_points('computer')
        for i in range(21):
            if i == 0:
                print("The bank's cards are:", end=" ")
            try:
                print(self.__Computer_cards[i][0] + " of " +
                      self.__Computer_cards[i][1], end=" ")
            except:
                print("\n")
                break

        if self.__computer_win_lose_condition() != None:
            return None
        if self.__Computer_points < self.Human_points:
            self.__Computer_cards.append(
                [self.possible_cards[randint(0, 12)], self.Suits[randint(0, 3)]])
            self.__computer_turn()

    def __computer_win_lose_condition(self):

        if self.__Computer_points > 21:
            print("The bank busted. Congratulations, you won " +
                  str(self.actual_bet * 2) + "€ :)")
            self.Actual_money += self.actual_bet
            self.__reset()
            return True
        elif self.__Computer_points > self.Human_points:
            print("I'm afraid you lose this game :(\n")
            self.Actual_money -= self.actual_bet
            self.__reset()
            return False
        elif self.__Computer_points == self.Human_points:
            print("Tie! :|\n")
            self.__reset()
            return False

    def __human_win_lose_condition(self):

        if self.Human_points == 21:
            self.Actual_money += self.actual_bet
            print("BLACKJACK. Congratulations, you won " +
                  str(self.actual_bet*2) + "€")
            self.__reset()
            return True
        elif self.Human_points > 21:
            self.Actual_money -= self.actual_bet
            print("Bust.\nI'm afraid you lose this game :(")
            self.__reset()
            return False

    def __human_turn(self):

        self.__update_points('human')
        self.__check_ace()
        if self.__human_win_lose_condition() != None:
            return None
        hit = input("Do you wanna hit? (y/n)\n")
        if hit == "y" or hit == "yes":
            self.Human_cards.append(
                [self.possible_cards[randint(0, 12)], self.Suits[randint(0, 3)]])


            for i in range(21):
                if i == 0:
                    print("Now, your cards are: ", end=" ")
                try:
                    print(self.Human_cards[i][0]
                          + " of " + self.Human_cards[i][1], end=", ")
                except:
                    print("\n")
                    break
            self.__human_turn()
        else:
            self.__computer_turn()

    def __update_points(self, selection):

        if selection == 'human':
            self.Human_points = sum([self.Cards[i[0]]
                                     for i in self.Human_cards])
        else:
            self.__Computer_points = sum(
                [self.Cards[i[0]] for i in self.__Computer_cards])

    def __reset(self):

        if self.Actual_money > 0:
            ask_user = input("Do yo want to play again? (y/n)\n")
            if ask_user == "y" or ask_user == "yes":
                self.__init__()
            else:
                print("Thanks for playing. Your final balance is " +
                      str(self.initial_money - self.Actual_money) + "\n")
        else:
            print("You have lost all you money, thanks for playing.")


Game1 = BlackJack()
