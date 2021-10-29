# Base for Deck and card values
import random
# creates list of suits
suit = ('Hearts','Dimonds','Spades','Clubs')
# creates list of ranks
rank = ('Two','Three','Four','Five','Six','Seven','Eight','Nine','Ten','Jack','Queen','King','Ace')

# need to fix ace to have value of 11 and one
# creates keys and values for card values as (int)
values = {'Two':2,'Three':3,'Four':4,'Five':5,'Six':6,'Seven':7,'Eight':8,'Nine':9,
          'Ten':10,'Jack':10,'Queen':10,'King':10,'Ace':11}

# create a class thatuses the list above and 
class Card:
    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]
        
    def __str__(self):
        return self.rank + ' of ' + self.suit


class Deck:
    def __init__(self):
        self.all_cards = []
        
        for suit in suits:
            for rank in ranks:
                created_card = Card(suit,rank)
                self.all_cards.append(created_card)
                
    def shuffle(self):
        random.shuffle(self.all_cards)
        print('All cards have been shuffled and are ready to Deal')
        
    def deal_one(self):
        return self.all_cards.pop()


def start_up():
    print('WELCOME TO BLACK JACK')
    
    player_name = ''
    while True:
        player_name = input('Please enter your name\n')
        if player_name.replace(' ','').isalpha() == True:
            break
        else:
            print('Please enter your name no numbers or special charcters')
            continue
    
    cash = ''
    while type(cash) != int:
        try:
            cash = int(input(f'How much money would you like to start with?'))
        except:
            print('Please enter a number nothing else')
            
    print(f'Great thanks now you have {cash} in your account')
    
    return player_name, cash


def play_deal():
    choice = ''
    while choice not in ['1','2']:
        choice = input('Please choose an option \nPlace a bet and Deal cards : press 1\nCash Out : press 2\n')
    return choice

# If 2 is the input then the following message will display and break out of all game
def cash_out():
    print(f'Thank you for playing here if you cash out : ${cash}')