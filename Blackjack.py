'''
    The 21 BlackJack, now in Python
'''
from time import sleep

from Deck import Deck
from Player import Player, get_my_Deck


def blackjack() -> None:
    """A multiplayer 21 BlackJack simulator. Just call this function, and enjoy!"""

    check_first_game = True
    my_deck = get_my_Deck()
    players = []
    computer_cards = my_deck.get_initial_cards()
    computer_points = Deck.sum_points(computer_cards)

    def initialization():
        nonlocal check_first_game
        if check_first_game:
            check_first_game = False
            try:
                number_of_people = int(
                    input("How many people are going to play? (1-5)\n"))
            except ValueError:
                print("Please, use only numbers.\n")
            for i in range(number_of_people):
                name = input("Please, enter your name, Player " + str(i + 1) +
                             "\n")
                for _ in range(5):
                    try:
                        initial_money = int(
                            input(
                                "How much money do you have? (Use only numbers)\n"
                            ))
                        players.append(Player(name, initial_money))
                        break
                    except ValueError:
                        print("Please, use only numbers.\n")

        start_game()

    def start_game():
        print("The game has started.\n")
        print("The first card of the bank is " + str(computer_cards[0]))
        for player in players:
            player_turn(player)
        computer_turn()

    def check_player_bet(player: Player):
        for _ in range(5):
            try:
                bet = int(input("What bet do you wanna make?\n"))
                if bet > player.get_actual_money():
                    print(
                        "Your bet cannot be greater than your actual money.\n")
                elif bet <= 0:
                    print("Your bet must be greater than 0.\n")
                else:
                    player.set_actual_bet(bet)
                    break

            except SyntaxError:
                print("Please, use only numbers.\n")

    def player_win_lose_condition(player: Player) -> bool:
        result = None
        if player.get_points() == 21:
            print("BLACKJACK")
            result = True
        elif player.get_points() > 21:
            player.loser_points()
            print("BUST.\nI'm afraid you lose this game :(\n")
            result = False

        return result

    def show_player_cards(player: Player):
        for i in range(21):
            if i == 0:
                print("Now, your cards are:", end=" ")
            try:
                print(player.get_cards()[i], end=", ")
            except IndexError:
                print()
                break

    def ask_if_hit(player: Player):
        for _ in range(21):
            sleep(2)
            if player_win_lose_condition(player) is None:
                decision = input("Do you wanna hit? (y/n)\n")
                if decision.strip().lower() == "y"\
                or decision.strip().lower() == "yes":
                    player.deal_card()
                    show_player_cards(player)
                else:
                    print(str(player) + " stanted")
                    break
            else:
                break

    def player_turn(player: Player):
        print("##############################################################################################################")
        print(
            str(player) + ", your actual money is " +
            str(player.get_actual_money()) + "€\n")
        check_player_bet(player)
        print("Your turn has started.\nYour cards are " +
              str(player.get_cards()[0]) + " and " +
              str(player.get_cards()[1]))
        sleep(2)
        ask_if_hit(player)

    def computer_win_lose_condition() -> bool:
        nonlocal computer_points
        if computer_points > 21:
            print("The bank busted. The game ended :)\n")
            computer_points = 1
            end_game()
            return True
        return False

    def show_computer_cards():
        nonlocal computer_cards
        for i in range(21):
            if i == 0:
                print("The bank cards are: ", end="")
            try:
                print(computer_cards[i], end=", ")
            except IndexError:
                print()
                break

    def computer_turn():
        nonlocal computer_cards, computer_points
        print("##############################################################################################################")
        print("Now it is the bank turn.\n")
        sleep(2)
        for _ in range(21):
            sleep(2)
            show_computer_cards()
            if not computer_win_lose_condition():
                if computer_points < 17:
                    print("The bank is going to hit a card\n")
                    computer_cards.append(my_deck.deal_card())
                    computer_points = Deck.sum_points(computer_cards)
                else:
                    print()
                    end_game()
                    break
            else:
                print()
                end_game()
                break
                
    def reset_computer_cards():
        nonlocal computer_cards, computer_points
        computer_cards = my_deck.get_initial_cards()
        computer_points = Deck.sum_points(computer_cards)
        
    def end_game():
        print("##############################################################################################################")
        for player in players:
            if player.get_points() == 21 or\
            player.get_points() > computer_points:
                player.update_actual_money(player.get_actual_bet())
                print(
                    str(player) + " won " + str(player.get_actual_bet() * 2) +
                    "€ :)\n")
            elif player.get_points() == computer_points:
                print(str(player) + ", it is a Tie! :|\n")
            else:
                player.update_actual_money(-player.get_actual_bet())
                print(str(player) + " lost against the bank :(\n")
        reset()

    def reset():
        print("##############################################################################################################")
        delete_players = []
        for player in players:
            final_balance = str(player.get_actual_money() -
                                player.get_initial_money()) + "€"
            if "-" not in final_balance:
                final_balance = "+" + final_balance
            if player.get_actual_money() > 0:
                decision = input(
                    str(player) + ", do you want to play again? (y/n)\n")
                if decision.strip().lower() == "y" or\
                decision.strip().lower() == "yes":
                    player.reset_cards()
                else:
                    print("Thanks for playing, " + str(player) +
                          " your final balance is " + final_balance + "\n")
                    delete_players.append(player)
            else:
                print(
                    str(player) +
                    ", you have lost all your money. Thanks for playing\n")
                delete_players.append(player)

        for player in delete_players:
            players.remove(player)

        if players:
            reset_computer_cards()
            initialization()

    initialization()


blackjack()
