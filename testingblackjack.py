# Base for Deck and card values
import random
# creates list of suits
suits = ('Hearts','Dimonds','Spades','Clubs')
# creates list of ranks
ranks = ('Two','Three','Four','Five','Six','Seven','Eight','Nine','Ten','Jack','Queen','King','Ace')

# need to fix ace to have value of 11 and one
# creates keys and values for card values as (int)
values = {'Two':2,'Three':3,'Four':4,'Five':5,'Six':6,'Seven':7,'Eight':8,'Nine':9,
          'Ten':10,'Jack':10,'Queen':10,'King':10,'Ace':11}


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


# Gonna try and make alot of defs for this problem
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


def bet(cash):
    bet_amount = ''
    while type(bet_amount) != int:
        try:
            bet_amount = int(input('how much would you like to bet'))
        except:
            print('Please enter a number nothing else')
    return bet_amount


def start_draw():
    
    player_hand = []
    dealer_hand = []
        # pulled hands is full to extend back to deck
    pulled_cards = []
    for cards in range(4):
        pulled_cards.append(my_deck.deal_one())

    player_hand.append(pulled_cards[0])
    dealer_hand.append(pulled_cards[1])
    player_hand.append(pulled_cards[2])
    dealer_hand.append(pulled_cards[3])


    player_total = player_hand[0].value + player_hand[1].value
    dealer_total = dealer_hand[0].value


    print(*player_hand, sep = ',')
    print(f'You have: {player_total}\nDealer has: {dealer_total}')

        # showing dealer total with both cards shown
    print(dealer_hand[0], ', Hidden Card')
    return player_hand, player_total, dealer_hand, dealer_total, pulled_cards


def win_21(bet_amount,cash,black_jack):
    if player_total == 21:
            print('Congrats you have Black Jack')
            bet_amount *= 1.5
            cash += bet_amount
            print(f'You have won {bet_amount} and you currently have {cash} in total')
            black_jack = True
    return cash, black_jack


def hit_stay():
    player_move = ''
    while True:
       # hit_stay = input
        player_move = input('Would you like to Hit or Stay?')
    
        if player_move in ['hit','Hit','stay','Stay']:
            player_move = player_move.capitalize()
            return player_move
        else:
            print('Please enter a valid word')


# something here is changing player_total to none type
def hit_one_card(player_total,player_hand):
    while True:
        pulled_cards.append(my_deck.deal_one())
        player_hand.append(pulled_cards[-1])
        player_total += player_hand[-1].value
        print(*player_hand, sep = ',')
        if player_total == 21:
            print('Congrats you have 21 lets see what the dealer has')
            return player_total
        elif player_total < 21:
            hit_again = input(f'you have a total of {player_total}\n would you like to Hit again? Y or N?')
            if hit_again.upper() == 'Y':
                pass
            elif hit_again.upper() == 'N':
                return player_total
            else:
                print('Please enter either Y or N')
        else:
            print(f'{player_total} :Sorry your over Dealer wins')
            player_total = 0
            return player_total


def dealer_turn(dealer_total,dealer_hand):
    dealer_total += dealer_hand[-1].value
    while True:
        print(*dealer_hand, sep = ',')
        print(f'Dealer has {dealer_total}')
        if dealer_total > 21:
            print('Dealer has busted')
            dealer_total = 0
            break
        elif dealer_total <= 21 and dealer_total >= 17:
            break
        else:
            pulled_cards.append(my_deck.deal_one())
            dealer_hand.append(pulled_cards[-1])
            dealer_total += dealer_hand[-1].value
            continue
    return dealer_total


def final_win(cash,bet_amount):
    win_cash = bet_amount
    if player_total > dealer_total:
        cash += win_cash
        print(f'Congrats you won {win_cash} and now have ${cash}')
        return cash
    elif dealer_total > player_total:
        cash -= win_cash
        print(f'Sorry you lose {win_cash} and now have ${cash}')
        return cash
    else:
        print('This was a draw')
        return cash


# Thinking about game logic
# Run first def to get name and amount of cash
player_name, cash = start_up()

while True:
# Run choice to have a choice number 1 or 2 fro play or cash out
    choice = play_deal()
    
    if choice == '1':
        my_deck = Deck()
        my_deck.shuffle()
        # If they choose to play then we will deal
        while True:
            
            while True:
            # need to get the players bet
                bet_amount = bet(cash)
                if bet_amount > cash:
                    print('You dont haver enough funds')
                    continue
                else:
                    break

                # will show the hand of player and one card of dealer
            player_hand, player_total, dealer_hand, dealer_total, pulled_cards = start_draw()

                # start as false to check and see if it changes to true meaning they won
            black_jack = False

            if player_total == 21:

                    # If they win black_jack set back to false to continue onto hit or stand
                cash, black_jack = win_21(bet_amount,cash,black_jack)
                break
                # if player wants to play after 1st two cards
            elif player_total < 21:
                move = hit_stay()

                    # if they stay then goto dealer play
                if move == 'Stay':
                    print(f'You are currently at {player_total} goodluck Dealers turn.')

                elif move == 'Hit':
                    player_total = hit_one_card(player_total,player_hand)

                    # dealer playing this gets skipped if player goes over 21
                dealer_total = dealer_turn(dealer_total,dealer_hand)

            elif player_total > 21:
                cash = final_win(cash,bet_amount)
                break

                    # checking final win or loss to dealer
            cash = final_win(cash,bet_amount)
            break
    elif choice == '2':
        cash_out()
        break