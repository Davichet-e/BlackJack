'''
    The 21 BlackJack, now in Python
'''
from Player import get_my_Deck, Player
from Deck import Deck


class BlackJack():
    __check_first_game = True
    __my_deck = get_my_Deck()
    __Players = []
    __counterComputer = 0

    def __init__(self):
        if self.__check_first_game:
            self.__check_first_game = False
            try:
                number_of_people = int(
                    input("How many people are going to play? (1-5)\n"))
            except ValueError:
                print("Please, use only numbers.\n")
            for i in range(number_of_people):
                name = input("Please, enter your name, Player " +
                             str(i + 1) + "\n")
                for _ in range(5):
                    try:
                        initial_money = float(
                            input("How much money do you have? (Use only numbers)\n"))
                        self.__Players.append(Player(name, initial_money))
                        break
                    except ValueError:
                        print("Please, use only numbers.\n")
        self.__computer_cards = self.__my_deck.get_initial_cards()
        self.__computer_points = Deck.sum_points(self.__computer_cards)
        self.__start_game()

    def __start_game(self):
        print("The game has started.\n")
        print("The first card of the bank is " + str(self.__computer_cards[0]))
        for player in self.__Players:
            BlackJack.__player_turn(player)
        self.__computer_turn()

    @staticmethod
    def __check_player_bet(player):
        for _ in range(5):
            bet = int(input("What bet do you wanna make?\n"))
            try:
                if bet > player.get_actual_money():
                    print("Your bet cannot be greater than your actual money.\n")
                elif bet <= 0:
                    print("Your bet must be greater than 0.\n")
                else:
                    player.set_actual_bet(bet)
                    break

            except SyntaxError:
                print("Please, use only numbers.\n")

    @staticmethod
    def __player_win_lose_condition(player):
        if player.get_points() == 21:
            print("BLACKJACK")
            return True
        elif player.get_points() > 21:
            player.loser_points()
            print("BUST.\nI'm afraid you lose this game :(\n")
            return False
        else:
            return None

    @staticmethod
    def __ask_if_hit(player):
        for _ in range(21):
            if BlackJack.__player_win_lose_condition(player) is None:
                decision = input("Do you wanna hit? (y/n)\n")
                if decision.strip().lower() == "y" or decision.strip().lower() == "yes":
                    player.deal_card()
                    for i in range(21):
                        if i == 0:
                            print("Now, your cards are:", end=" ")
                        try:
                            print(player.get_cards()[i], end=", ")
                        except IndexError:
                            print()
                            break
                else:
                    print(str(player) + " stanted")
                    break
            else:
                break

    @staticmethod
    def __player_turn(player):
        print(str(player) + ", your actual money is " +
              str(player.get_actual_money()) + "€\n")
        BlackJack.__check_player_bet(player)
        print("Your turn has started.\nYour cards are " +
              str(player.get_cards()[0]) + " and " + str(player.get_cards()[1]))
        BlackJack.__ask_if_hit(player)

    def __computer_win_lose_condition(self):
        if self.__computer_points > 21:
            print("The bank busted. The game ended :)\n")
            self.__computer_points = 1
            self.__end_game()
            return True
        return False

    def __computer_turn(self):
        print("Now it is the bank turn.\n")
        for _ in range(21):
            for i in range(21):
                if i == 0:
                    print("The bank cards are: ", end="")
                try:
                    print(self.__computer_cards[i], end=", ")
                except IndexError:
                    print()
                    break
            if not self.__computer_win_lose_condition():
                if self.__computer_points < 17:
                    print("The bank is going to hit a card\n")
                    self.__computer_cards.append(self.__my_deck.deal_card())
                    self.__computer_points = Deck.sum_points(
                        self.__computer_cards)
                else:
                    self.__end_game()
                    break
            else:
                self.__end_game()
                break

    def __end_game(self):
        for player in self.__Players:
            if player.get_points() == 21 or player.get_points() > self.__computer_points:
                player.update_actual_money(player.get_actual_bet())
                print(str(player) + " won " +
                      str(player.get_actual_bet() * 2) + "€ :)\n")
            elif player.get_points() == self.__computer_points:
                print("It is a Tie! :|\n")
            else:
                player.update_actual_money(-player.get_actual_bet())
                print(str(player) + " lost against the bank :(\n")
        self.__reset()

    def __reset(self):
        for player in self.__Players:
            final_balance = str(player.get_actual_money() -
                                player.get_initial_money()) + "€"
            if "-" not in final_balance:
                final_balance = "+" + final_balance
            if player.get_actual_money() > 0:
                decision = input(
                    str(player) + ", do you want to play again? (y/n)\n")
                if decision.strip().lower() == "y" or decision.strip().lower() == "yes":
                    player.reset_cards()
                else:
                    print("Thanks for playing, " + str(player) +
                          " your final balance is " + final_balance + "\n")
                    self.__Players.remove(player)
            else:
                print(str(player) +
                      ", you have lost all your money. Thanks for playing\n")
                self.__Players.remove(player)
        if self.__Players:
            self.__init__()


GAME1 = BlackJack()
