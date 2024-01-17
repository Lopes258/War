import Cards
import random


#CREATE THE PLAYERS
class Player:

    def __init__(self,name):

        self.name = name
        self.all_cards = []

    def remove_one(self):
        return self.all_cards.pop(0)

    def add_cards(self,new_cards):
        if type(new_cards) == type([]):
            self.all_cards.extend(new_cards)
        else:
            self.all_cards.append(new_cards)

    def __str__(self):
        return f'Player {self.name} has {len(self.all_cards)} cards.'
    
#GAME SETUP

player_one = Player('One')
player_two = Player('Two')

new_deck = Cards.Deck()
new_deck.shuflle()


for x in range(26):
    player_one.add_cards(new_deck.deal_one())
    player_two.add_cards(new_deck.deal_one())

game_on = True


round_num = 0
war_count = 0

while game_on:

    round_num += 1
    print(f"Round {round_num}")

    if len(player_one.all_cards) == 0:
        print("Player One, out of cards! Player Two Wins!")
        game_on = False
        break

    if len(player_two.all_cards) == 0:
        print("Player Two, out of cards! Player One Wins!")
        game_on = False
        break

##START A NEW ROUND
    player_one_cards = []
    player_one_cards.append(player_one.remove_one())

    player_two_cards = []
    player_two_cards.append(player_two.remove_one())


# while at_war
    at_war = True

    while at_war:
        #I'M USING -1 IN THIS CASE BECAUS IN CASE OF WAR I DON'T CHOOSE THE FIRST CARD AGAIN TO STAR A NEW COMPARISON
        if player_one_cards[-1].values > player_two_cards[-1].values:

            player_one.add_cards(player_one_cards)
            player_one.add_cards(player_two_cards)

            at_war = False
        
        elif player_two_cards[-1].values > player_one_cards[-1].values:

            player_two.add_cards(player_one_cards)
            player_two.add_cards(player_two_cards)

            at_war = False

        else:
            print('WAR!')

            if len(player_one.all_cards) < 5:
                print("Player One unable to declare war")
                print("PLAYER TWO WINS!")
                game_on = False
                break

            elif len(player_two.all_cards) < 5:
                print("Player Two unable to declare war")
                print("PLAYER ONE WINS!")
                game_on = False
                break

            else: 
                for num in range(5):
                    player_one_cards.append(player_one.remove_one())
                    player_two_cards.append(player_two.remove_one())