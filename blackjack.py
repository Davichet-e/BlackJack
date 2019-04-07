'''The 21 BlackJack, now in Python. '''

from time import sleep

from deck import Deck
from player import Player, get_my_Deck


def blackjack() -> None:
    """A multiplayer 21 BlackJack simulator. Just call this function, and enjoy!"""

    check_first_game = True
    my_deck = get_my_Deck()
    players = []
    dealer_cards = my_deck.get_initial_cards()
    dealer_points = Deck.sum_points(dealer_cards)

    #---------------------------------------------------------------------------------#
    def initialization():
        nonlocal check_first_game
        print("#########################################\tGame Started\t   \
#########################################")
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
                    except ValueError:
                        print("Please, use only numbers.\n")
                    else:
                        players.append(Player(name, initial_money))
                        break
        game()

    def game():
        print("The game has started.\n")
        print(f"The first card of the dealer is {str(dealer_cards[0])}")
        for player in players:
            player_turn(player)
        dealer_turn()
        end_game()
        reset()

    def check_player_bet(player: Player):
        for _ in range(5):
            try:
                bet = int(input("What bet do you wanna make?\n"))
            except SyntaxError:
                print("Please, use only numbers.\n")
            else:
                if bet > player.get_actual_money():
                    print(
                        "Your bet cannot be greater than your actual money.\n")
                elif bet <= 0:
                    print("Your bet must be greater than 0.\n")
                else:
                    player.set_actual_bet(bet)
                    break

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
                or decision.strip().lower() == "yes"\
                or decision.strip().lower() == "true"\
                or decision.strip().lower() == "1":
                    player.deal_card()
                    show_player_cards(player)
                else:
                    print(str(player) + " stanted")
                    break
            else:
                break

    def player_turn(player: Player):
        print(
            f"#########################################\t{str(player)}'s turn\t   \
#########################################")
        print(
            f"{str(player)}, your actual money is {str(player.get_actual_money())} €\n"
        )
        check_player_bet(player)
        print("Your turn has started.\nYour cards are: ")
        print(f"{str(player.get_cards()[0])} and {str(player.get_cards()[1])}")
        print()
        sleep(1)
        ask_if_hit(player)

    def dealer_win_lose_condition() -> bool:
        nonlocal dealer_points
        if dealer_points > 21:
            print("The dealer busted. The game ended :)\n")
            dealer_points = 1
            return True
        return False

    def show_dealer_cards():
        nonlocal dealer_cards
        for i in range(21):
            if i == 0:
                print("The dealer cards are: ", end="")
            try:
                print(dealer_cards[i], end=", ")
            except IndexError:
                print()
                break

    def dealer_turn():
        nonlocal dealer_cards, dealer_points
        print("#########################################\tDealer's Turn\t   \
#########################################")
        sleep(2)
        for _ in range(21):
            sleep(2)
            show_dealer_cards()
            if not dealer_win_lose_condition():
                if dealer_points < 17:
                    print("The dealer is going to hit a card\n")
                    dealer_cards.append(my_deck.deal_card())
                    dealer_points = Deck.sum_points(dealer_cards)
                else:
                    print()
                    break
            else:
                print()
                break

    def reset_dealer_cards():
        nonlocal dealer_cards, dealer_points
        dealer_cards = my_deck.get_initial_cards()
        dealer_points = Deck.sum_points(dealer_cards)

    def end_game():
        print("#########################################\tResults\t      \
##############################################")
        for player in players:
            if player.get_points() == 21\
            or player.get_points() > dealer_points:
                player.update_actual_money(player.get_actual_bet())
                print(
                    f"{str(player)} won {str(player.get_actual_bet() * 2)}€ :)\n"
                )
            elif player.get_points() == dealer_points:
                print(f"{str(player)}, it is a Tie! :|\n")
            else:
                player.update_actual_money(-player.get_actual_bet())
                print(f"{str(player)} lost against the dealer :(\n")
        sleep(1)

    def reset():
        print("#########################################\tGame Finished\t   \
#########################################")
        delete_players = []
        for player in players:
            final_balance = f"{str(player.get_actual_money() - player.get_initial_money())} €"
            if "-" not in final_balance:
                final_balance = "+" + final_balance
            if player.get_actual_money() > 0:
                decision = input(
                    str(player) + ", do you want to play again? (y/n)\n")
                if decision.strip().lower() == "y"\
                or decision.strip().lower() == "yes"\
                or decision.strip().lower() == "true"\
                or decision.strip().lower() == "1":
                    player.reset_cards()
                else:
                    print(
                        f"Thanks for playing, {str(player)} your final balance is {final_balance}\n"
                    )
                    delete_players.append(player)
            else:
                print(
                    f"{str(player)} , you have lost all your money. Thanks for playing\n"
                )
                delete_players.append(player)

        for player_to_delete in delete_players:
            players.remove(player_to_delete)

        if players:
            reset_dealer_cards()
            initialization()

    #---------------------------------------------------------------------------------#

    initialization()


blackjack()
