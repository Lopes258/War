
import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':11, 'Queen':12, 'King':13, 'Ace':14}

#CREATE THE CARDS
class Card:
    #HERE IS THE MERGE TO CREATE THE CARD
    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
        self.values = values[rank]
    #IF YOU WANT TO WHAT IS THE CARD
    def __str__(self):
        return self.rank + ' of ' + self.suit

#CREATE ALL THE 56 CARDS
class Deck:
    #TO CREATE THE ALL CARDS
    def __init__(self):

        self.all_cards = []

        for suit in suits:
            for rank in ranks:

                created_card = Card(suit,rank)

                self.all_cards.append(created_card)
    #SO DECK CAN BE SHUFLE IN THAT WAY THE CARDS WILL BE PICK AT RANDOM
    def shuflle(self):

        random.shuffle(self.all_cards)
    #TO PICK THE CARDS
    def deal_one(self):
        return self.all_cards.pop()
    
 