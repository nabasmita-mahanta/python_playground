# Game setup
from Udemy.Milestone_Project_2.Deck_class import Deck
from Udemy.Milestone_Project_2.Player_class import Player

# creating two players
print("-------PLAYERS-------")
player1 = Player("Puku")
player2 = Player("Kupu")

print(f"Players Created : {player1.name} and {player2.name}")
print(player1)
print(player2)

print("-------DECK-------")
# creating a deck
new_deck = Deck()
# shuffling a deck
new_deck.shuffle()

# printing total cards in deck
print(f"Deck Created. Cards Present: {len(new_deck.all_cards)}")

print("-------Assigning Cards from Deck to Players-------")
# As there are 52 cards in deck and we have 2 players. Each player will get 26 cards.
for x in range(26):
    player1.add_cards(new_deck.deal_one())
    player2.add_cards(new_deck.deal_one())

print(player1)
print(player2)

print("-------Now the game is on-------")

game_is_on = True
round_num = 0

while game_is_on:
    round_num = round_num + 1
    print(f"Current round = {round_num}")

    # Check if any player has zero cards
    if len(player1.all_cards) == 0:
        print(f"Player1- {player1.name} has no cards left, \nPlayer2- {player2.name} wins.")
        game_is_on = False
        break
    if len(player2.all_cards) == 0:
        print(f"Player2- {player2.name} has no cards left, \nPlayer1- {player1.name} wins.")
        game_is_on = False
        break

    # Game is still on, start another round
    player1_cards = []
    player1_cards.append(player1.remove_one())
    player2_cards = []
    player2_cards.append(player2.remove_one())

    # Comparing the top cards from each player

    at_war = True

    while at_war:
        # print("Comparing the top cards from each player")
        top_player1_card = player1_cards[-1]
        top_player2_card = player2_cards[-1]
        # Comparing -
        if top_player1_card.values > top_player2_card.values:
            print("Player1 gets all the cards of player2")
            player1.add_cards(player1_cards)
            player1.add_cards(player2_cards)
            at_war = False
        elif top_player1_card.values < top_player2_card.values:
            print("Player2 gets all the cards of player1")
            player2.add_cards(player1_cards)
            player2.add_cards(player2_cards)
            at_war = False
        else:
            print("WAR !! Both cards are equal, each player has to submit 5 more cards")
            # both players give 5 more cards
            if len(player1.all_cards) < 5:
                print(f"Player1 ({player1.name}) does not have 5 cards. Player2 ({player2.name}) wins")
                at_war = False
                game_is_on = False
                break
            elif len(player2.all_cards) < 5:
                print(f"Player2 ({player2.name}) does not have 5 cards. Player1 ({player1.name}) wins")
                at_war = False
                game_is_on = False
                break
            else:
                for num in range(5):
                    player1_cards.append(player1.remove_one())
                    player2_cards.append(player2.remove_one())
