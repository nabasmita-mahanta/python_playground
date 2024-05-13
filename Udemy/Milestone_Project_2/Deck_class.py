import random

from Udemy.Milestone_Project_2.Card_class import Card
import GLOBAL

class Deck:

    def __init__(self):

        self.all_cards = []

        for suit in GLOBAL.suits:
            for rank in GLOBAL.ranks:
                # Create the Card Object
                created_card = Card(suit, rank)
                self.all_cards.append(created_card)

    def shuffle(self):
        random.shuffle(self.all_cards)

    def deal_one(self):
        return self.all_cards.pop()
