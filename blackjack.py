"""
The 21 BlackJack now in python!
"""
from time import sleep
from typing import List, Optional

from player import Player
from hand import Hand
from deck import Deck

###########################################################################################

DECK: Deck
DEALER_HAND: Hand
PLAYERS: List[Player] = []


###########################################################################################


def blackjack() -> None:
    """A multiplayer 21 BlackJack simulator. Just call this function, and enjoy!"""
    global DECK, DEALER_HAND

    print("This BlackJack Game has been created by David Garcia Morillo")
    # Initialize `DECK` and `DEALER_HAND`
    while True:
        try:
            n_of_decks = int(input("How many decks do you want to use (4-8)\n> "))
        except ValueError:
            print("Please, use only numbers.\n")
        else:
            if not 3 < n_of_decks <= 8:
                print("The number of decks must be between 4 and 8\n")
            else:
                break

    DECK = Deck(n_of_decks)
    DEALER_HAND = Hand(DECK)

    start_game()

    while True:
        print("###### Game Started ######\n")

        print(f"The first card of the dealer is {DEALER_HAND.cards[0]}")

        for player in PLAYERS:
            player_turn(player)

        dealer_turn()
        end_game()
        if not next_game():
            break


###########################################################################################


def start_game() -> None:
    """Starts the game"""
    number_of_people: int = ask_number_of_people()
    ask_and_set_player_attributes(number_of_people)


def ask_number_of_people() -> int:
    """Ask how many people it is going to start playing the game"""
    while True:
        try:
            number_of_people: int = int(
                input("How many people are going to play? (1-5)\n> ")
            )
        except ValueError:
            print("Please, use only numbers.\n")
        else:
            if not 0 < number_of_people <= 5:
                print("The number of people must be between 1 and 5\n")
            else:
                break

    return number_of_people


def ask_and_set_player_attributes(num_of_people: int) -> None:
    """Ask the players their names and initial money and
    pass them to the 'Player' class"""
    for i in range(num_of_people):
        name: str = input(f"Please, enter your name, Player {i + 1}\n> ")
        while True:
            try:
                initial_money = int(
                    input("How much money do you have? (Use only numbers)\n> ")
                )

            except ValueError:
                print("Please, use only integer values.\n")

            else:

                if initial_money < 50:
                    print("The initial money must be greater or equal than 50\n")
                else:
                    PLAYERS.append(Player(name, initial_money, DECK))
                    break


def ask_player_bet(player: Player) -> None:
    """Ask the player received as paramater what bet does he/she wanna make"""
    while True:
        try:
            bet = int(input("What bet do you wanna make?\n> "))

        except ValueError:
            print("Please, use only integer values.\n")

        else:
            if bet > player.actual_money:
                print("Your bet cannot be greater than your actual money.\n")

            elif bet <= 0:
                print("Your bet must be greater than 0.\n")

            else:
                player.actual_bet = bet
                break


def hand_win_or_lose(hand: Hand) -> bool:
    """Checks if the player received as paramater won or lost"""
    result: bool = False
    hand_points: int = hand.points
    if hand_points == 21:
        if hand.has_blackjack():
            print("BLACKJACK!")
        else:
            print("YOU GOT 21 POINTS!")

        result = True

    elif hand_points == 0:
        print("BUST.\nI'm afraid you lose this game :(\n")
        result = True

    return result


def check_if_yes(user_decision: str) -> bool:
    """Checks if the player decision is affirmative"""
    return user_decision.strip().lower() in {"y", "yes", "1", "true"}


def ask_player_action() -> bool:
    """Ask the player if he/she wants to hit"""
    sleep(2)

    decision = input("What do you want to do?\n> ")
    return check_if_yes(decision)


def player_turn(player: Player) -> None:  # FIXME
    """TODO"""
    print(f"###### {player}'s turn ######\n")
    print(f"{player}, your actual money is {player.actual_money} €\n")

    ask_player_bet(player)

    print("Your cards are: ")
    print(
        f"{player.hands[0].cards[0]} and {player.hands[0].cards[1]} "
        f"({player.hands[0].points} points)"
    )
    print()
    sleep(1)

    has_doubled: bool = False
    has_splitted: bool = False
    for i, hand in enumerate(player.hands):
        # If the player has doubled, he can only hit one more time
        while not hand_win_or_lose(hand) and (not has_doubled or len(hand.cards) < 3):
            if has_splitted:
                print(f"(Hand #{i})")
                print(f"Your cards are {hand}")

            user_decision: str = input(
                "\nWhat do you want to do?"
                "\nAvailable Commands: (h)it, (s)tand, (sp)lit, (d)ouble, (surr)ender\n> "
            ).strip().lower()

            if user_decision in ("h", "hit"):
                player.hit(hand_index=i)
                print(f"Now, your cards are: {hand}")

            elif user_decision in ("s", "stand"):
                print(f"{player} stood")
                break

            elif user_decision in ("sp", "split"):
                if not has_doubled:
                    error_message: Optional[str] = player.split()
                    if error_message:
                        print(error_message)
                    else:
                        has_splitted = True
                        print("You have splitted the hand!")

                else:
                    print("You cannot split because you have already doubled")

            elif user_decision in ("d", "double"):
                if not has_doubled:
                    error_message: Optional[str] = player.double()
                    if error_message:
                        print(error_message)
                    else:
                        has_doubled = True
                        print("You have doubled the hand!")
                else:
                    print("You cannot double because you have already doubled")

            elif user_decision in ("surr", "surrender"):
                if not has_doubled:
                    error_message: Optional[str] = player.surrender()
                    if error_message:
                        print(error_message)
                    else:
                        print("You have surrendered!")
                else:
                    print("You cannot double because you have already doubled")

            else:
                print(
                    "Invalid command!\nAvailable Commands: (h)it, (s)tand, (sp)lit, (d)ouble, (surr)ender"
                )


def dealer_lost() -> bool:
    """Check if the dealer lost"""
    if DEALER_HAND.points == 0:
        print("The dealer busted. The game ended :)\n")
        return True
    return False


def dealer_turn() -> None:
    """Reproduce the dealer turn"""
    print("###### Dealer's Turn ######\n")
    sleep(2)
    print(f"The dealer's cards are {DEALER_HAND.cards[0]} and {DEALER_HAND.cards[1]}\n")

    while not dealer_lost() and DEALER_HAND.points < 17:
        sleep(2)
        print("The dealer is going to hit a card\n")
        DEALER_HAND.deal_card()
        sleep(1)
        print(f"Now, the dealer's cards are: {DEALER_HAND}")


def end_game() -> None:
    """Checks which player wins or loses, and manage their money according to that"""
    print("###### Results ######\n")
    dealer_points: int = DEALER_HAND.points

    for player in PLAYERS:
        for i, hand in enumerate(player.hands):
            hand_points: int = hand.points
            if hand_points > dealer_points or (
                hand.has_blackjack() and not DEALER_HAND.has_blackjack()
            ):
                money_earned: int = player.win()

                hand_specification = ""
                if len(player.hands) == 1:
                    hand_specification = f" (#{i + 1} hand)"

                print(f"{player}{hand_specification} won {money_earned}€ :)\n")
            # Checks if the player points are 0 or if they are less than the dealer's ones
            elif hand_points == 0 or hand_points < dealer_points:
                player.lose()
                print(f"{player} lost against the dealer :(\n")

            else:
                print(f"{player}, it is a tie! :|\n")
    sleep(1)


def ask_if_next_game(player: Player) -> bool:
    """Ask a player if he/she wants to play another game"""
    player_next_game: bool = False
    final_balance: str = f"{player.actual_money - player.initial_money} €"
    # Check if 'final_balance' is negative, if not, adds a '+' sign
    if "-" not in final_balance:
        final_balance = "+" + final_balance

    if player.actual_money > 0:
        decision: str = input(f"{player}, do you want to play again? (y/n)\n> ")

        if check_if_yes(decision):
            player.reset_hands()
            player_next_game = True

        else:
            print(
                (
                    f"Thanks for playing, {player}"
                    f" your final balance is {final_balance}\n"
                )
            )

    else:
        print(f"{player}, you have lost all your money. Thanks for playing\n")

    return player_next_game


def next_game() -> bool:  # FIXME
    """Check if there are players for a next game"""
    global PLAYERS

    print("###### Game Finished ######\n")

    PLAYERS = [player for player in PLAYERS if ask_if_next_game(player)]

    print("\n\n\n\n\n")

    if PLAYERS:
        DEALER_HAND.initialize_attributes()
        return True

    return False


if __name__ == "__main__":
    blackjack()
