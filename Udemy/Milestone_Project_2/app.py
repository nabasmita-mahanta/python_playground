from Udemy.Milestone_Project_2.Card_class import Card
from Udemy.Milestone_Project_2.Deck_class import Deck
from Udemy.Milestone_Project_2.Player_class import Player

# Creating 2 predefined cards
three_of_clubs = Card("Clubs", "Three")
print(three_of_clubs.rank)
print(three_of_clubs.suit)

two_of_hearts = Card("Hearts", "Two")
print(two_of_hearts.values)
print(two_of_hearts.rank)
print(two_of_hearts.suit)

print(two_of_hearts == three_of_clubs)

# Creating a Deck
new_deck = Deck()
# shuffling the deck twice
new_deck.shuffle()
new_deck.shuffle()

mycard = new_deck.deal_one()

print(mycard)
print(len(new_deck.all_cards))
# bottom_card = new_deck.all_cards[-1]
#
# for card_object in new_deck.all_cards:
#     print(card_object)

print("----------------PLAYER------------------")
# Creating a player
new_player = Player('Puku')
print(new_player)
# Adding a pre defined card to the player
new_player.add_cards(three_of_clubs)
print(new_player)
print(new_player.all_cards[0])
# Taking out three cards from the deck
card1 = new_deck.deal_one()
card2 = new_deck.deal_one()
card3 = new_deck.deal_one()

# Adding above three cards to the player
new_player.add_cards([card1,card2,card3])
print(new_player)

# printing all cards of the player
for card in new_player.all_cards:
    print(card)

# removing one card
new_player.remove_one()
print(new_player)



