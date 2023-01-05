import random
from cardvalues import *


class Card():
    #suit , rank , value 
    def __init__(self,suit,rank):
        self.suit = suit.lower()
        self.rank = rank.lower()
        self.value = values[rank]
    def __str__(self):
        return self.rank + ' of ' + self.suit

class Deck():

    def __init__(self):
        
        self.all_cards = []

        for suit in suits:
            for rank in ranks:
                #CREATE CARD OBJ
                created_card = Card(suit,rank) #each item in suit and rank dict
                self.all_cards.append(created_card)

    def shuffle(self):
        random.shuffle(self.all_cards)

    def deal_one(self):
        return self.all_cards.pop()

class Player():

    def __init__(self , name):
        self.name = name
        self.all_cards = []

    def remove_one(self):
         return self.all_cards.pop(0)

    def add_cards(self , new_cards):
        if type(new_cards) == type([]):
            self.all_cards.extend(new_cards)
        else:
            self.all_cards.append(new_cards)
        
    def __str__(self):
            return f'Player {self.name} has {len(self.all_cards)} cards'


#Creating players
player_one = Player("one")
player_two = Player("two")

new_deck = Deck()
new_deck.shuffle()

for x in range(26):
    player_one.add_cards(new_deck.deal_one())
    player_two.add_cards(new_deck.deal_one())

game_on = True
round_num = 0
while game_on:
    round_num +=1
    print(f'Round {round_num}')


    if len(player_one.all_cards) == 0:
        print('Player One, out of cards!')
        game_on = False
        break

    if len(player_one.all_cards) == 0:
        print('Player One, out of cards!')
        game_on = False
        break
    
    #Start a new round

    player_one_cards = []
    player_one_cards.append(player_one.remove_one())
    player_two_cards = []
    player_two_cards.append(player_two.remove_one())

    at_war = True
    
    while at_war:
        if player_one_cards[-1].value > player_two_cards[-1].value:

            player_one.add_cards(player_one_cards)
            player_one.add_cards(player_two_cards)
            at_war = False

        elif player_two_cards[-1].value > player_one_cards[-1].value:

            player_two.add_cards(player_two_cards)
            player_two.add_cards(player_one_cards)
            at_war = False
        
        else:
            print('WAR')
            if len(player_one.all_cards) < 5:
                print("Player One unable to go to war, player 2 wins")
                game_on = False
                break

            elif len(player_two.all_cards) < 5:
                print("Player two unable to go to war, player 1 wins")
                game_on = False
                break
            
            else:
                for num in range(3):
                    player_one_cards.append(player_one.remove_one())
                    player_two_cards.append(player_two.remove_one())

        



    















