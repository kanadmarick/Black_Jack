class Card:
    # A card must have a suit
    # A card must have a rank
    # A card must have a colour
    values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8,
              'Nine': 9, 'Ten': 10, 'Jack': 10, 'Queen': 10, 'King': 10, 'Ace': 11}

    def __init__(self, suit, rank):
        self.suit = suit.title()
        
        self.rank = rank.title()

    def __str__(self):
        return self.rank + ' ' + 'of' + ' ' + self.suit  # Example: Ace of Spades

    def return_color(self):
        # Returns the color of the card
        if self.suit in ['Hearts', 'Diamonds']:
            return 'This is a Red Card'
        else:
            return 'This is a Black Card'

    def is_face_card(self):
        # Returns true for face cards
        return self.rank in ['King', 'Queen', 'Joker']

    def return_value(self, total=0):
        #if self.rank=='Ace':
         #   if total+11 >21:
          #      return (total-10)
           # else:
            #    return 11
        #else:
            return Card.values[self.rank]

        
        
import random

class Deck:
    suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
    ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
    values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8,
              'Nine': 9, 'Ten': 10, 'Jack': 10, 'Queen': 10, 'King': 10, 'Ace': 11}

    def __init__(self):
        self.full = []
        for i in range(6):
            for suit in Deck.suits:
                for rank in Deck.ranks:
                    self.full.append(Card(suit, rank))  # Creates a full stack of cards

    def shuffle(self):
        random.shuffle(self.full)  # Does not return anything

    def one_deal(self):
        return self.full.pop()  # Removes one card from the list of all cards

    def divide_cards(self, players_num):
        # Divide the stack into the players
        players = {1: [], 2: [], 3: [], 4: [], 5: [], 6: []}
        self.full_deck()
        self.shuffle()
        for n in range(1, players_num + 1):
            for i in range(int(52 / players_num)):
                players[n].append(self.one_deal())
        return players

    
class Player:
    return_rate = 1.5
    def __init__(self, name, bankroll):
        self.hand = []
        self.name = name
        self.bankroll = bankroll
        self.bet = 0
        
    def win(self):
        self.bankroll += int(self.bet*Player.return_rate)
        return self.bankroll
    
    def bust(self):
        self.bankroll -= int(self.bet)
        return self.bankroll
    
    def draw(self):
        return self.bankroll
    
    def blackjack(self):
        return (sum(card.return_value() for card in self.hand)==21)
    
    def remove_card(self):
        # Removes the top card from the hand
        return self.hand.pop(0)

    def add_cards(self, new_cards):
        if type(new_cards) == list:
            self.hand.extend(new_cards)
        else:
            self.hand.append(new_cards)
        
    #def total_value(self):
      #  for i in range(len(self.hand)):
            
    def hand_values(self):
        total =0
        #print(f'{self.name}, you have the following cards:\n')
        for card in self.hand:
            
            total += card.return_value()
            #print(card)
            #print(total)
        if any(card.rank=='Ace' for card in self.hand):
            count = [card for card in self.hand if card.rank =='Ace']
            #if total>25:
                
             #   total -= 10*len(count)
            if total >21                                                                                                                                      :
                total -=10
        #print(f'Total value: {total}')
        return total  
    
    def display(self):
        print(f'{self.name}, you have the following cards:')
        
        for card in self.hand:
                print(card)
        print(f'Total value: {self.hand_values()}')
        print(f'Betting Amount: $ {self.bet}')
        print(f'Bank Roll: $ {self.bankroll}')
    def __str__(self):
        return f'Player {self.name} has {len(self.hand)} cards.'
    
    
    
class Dealer:
    def __init__(self):
        self.hand =[]
        
    
    def blackjack(self):
        return (sum(card.return_value() for card in self.hand)==21)
    
    def remove_card(self):
        # Removes the top card from the hand
        return self.hand.pop(0)

    def add_cards(self, new_cards):
        if type(new_cards) == list:
            self.hand.extend(new_cards)
        else:
            self.hand.append(new_cards)
        
    #def total_value(self):
      #  for i in range(len(self.hand)):
            
    def hand_values(self):
        total =0
        #print('Dealer has the following cards:\n')
        for card in self.hand:
            
            total += card.return_value()
            #print(card)
            #print(total)
        if any(card.rank=='Ace' for card in self.hand):
            count = [card for card in self.hand if card.rank =='Ace']
            #if total>25:
                
                #total -= 10*len(count-1)
            if total >17:
                total -=10
        #print(f'Total value: {total}')
        
        return total
        
    def display(self):
        print('The dealer has the following card(s):')
        if len(self.hand)>2:
            for card in self.hand:
                print(card)
            print(f'Total value: {self.hand_values()}')        
            
        else:
            print(self.hand[0])
            
def game_play(player):
    
    if player.hand[0].suit==player.hand[1].suit and len(player.hand)==2 and player.bet<((player.bankroll-10)/2):
                wrong = True
                while wrong:
                    play = input(f'{player.name}, please enter split, double, hit or stand: ').title()
                    if play in ['Split', 'Double' , 'Hit', 'Stand']:
                        wrong = False
    elif len(player.hand)==2 and player.bet<((player.bankroll-10)/2):
        wrong = True
        while wrong:
            play = input(f'{player.name}, please enter double, hit or stand: ').title()
            if play in ['Double' , 'Hit', 'Stand']:
                wrong = False
    else:
        wrong = True
        while wrong:
            play = input(f'{player.name}, please enter hit or stand: ').title()
            if play in ['Hit', 'Stand']:
                wrong = False
                
    if play=='Split':
        player.bet = player.bet*2
        player.add_cards(deck.one_deal())
        player.add_cards(deck.one_deal())
        player.display()
    elif play == 'Double':
        player.bet =player.bet*2
        player.add_cards(deck.one_deal())
        player.add_cards(deck.one_deal())
        player.display()
    elif play == 'Hit':
        player.add_cards(deck.one_deal())
        player.display()
    elif play == 'Stand':
        return False
    
    
def dealer_func():
    print('The dealer has the following cards:')
    dealer.hand_values()
    for card in dealer.hand:
        print(card)
    if dealer.hand_values()==21:
        print('Dealer has Black Jack!')
        for player in players:
            if player.hand_values()==21:
                print(f'Its a tie for {player.name}!')
                player.display()
            else:
                player.bust()
                print(f'{player.name} you lose!')
                print(f'You lost $ {player.bet}')
                player.display()
            
    elif dealer.hand_values()<17:
        print('Dealer is taking cards as value of hand is less than 17')
        while dealer.hand_values()<17:
            dealer.add_cards(deck.one_deal())
            dealer.hand_values()
        dealer.display()
        if dealer.hand_values()==21:
            for player in players:
                if player.hand_values()==21:
                    print(f'Its a tie for {player.name}!')
                    player.display
                else:
                    player.bust()
                    print(f'{player.name} you lose!')
                    print(f'You lost $ {player.bet}')
                    player.display()        
        elif dealer.hand_values() >21:
            print('Dealer bust!')
            for player in players:
                if player.hand_values()<=21:
                    player.win()
                    print(f'{player.name} you won!')
                    player.display()
                else:
                    player.bust()
                    print(f'{player.name} lost $ {player.bet}!')
                    player.display()
        elif dealer.hand_values() in range(17,21):
            for player in players:
                if player.hand_values() < dealer.hand_values():
                    player.bust()
                    print(f'{player.name} you lose!')
                    print(f'You lost $ {player.bet}')
                    player.display()
                elif player.hand_values() == dealer.hand_values():
                    print(f'Its a tie for {player.name}!')
                    player.display()
                elif player.hand_values() > dealer.hand_values() and player.hand_values()<=21:
                    player.win()
                    print(f'{player.name} you win!')
                    print(f'You won $ {player.bet}')
                    player.display()
                else:
                    player.bust()
                    print(f'{player.name} you lose!')
                    print(f'You lost $ {player.bet}')
                    player.display()
        
    elif dealer.hand_values() in range(17,21):
            for player in players:
                if player.hand_values() < dealer.hand_values():
                    player.bust()
                    print(f'{player.name} you lose!')
                    print(f'You lost $ {player.bet}')
                    player.display()
                elif player.hand_values() == dealer.hand_values():
                    print(f'Its a tie for {player.name}!')
                    player.display()
                elif player.hand_values() > dealer.hand_values() and player.hand_values()<=21:
                    player.win()
                    print(f'{player.name} you win!')
                    print(f'You won $ {player.bet}')
                    player.display()
                else:
                    player.bust()
                    print(f'{player.name} you lose!')
                    print(f'You lost $ {player.bet}')
                    player.display()
    
def one_round(players):
    # Betting amount module
    for player in players:
        print(f'{player.name}, you have $ {player.bankroll}')
        wrong = True
        while wrong:
            player.bet = int(input(f'{player.name}, please enter your betting amount (between $ 10 and $ {player.bankroll}):\n'))
            if player.bet in range(10, player.bankroll+1):
                
                wrong = False
            else:
                wrong = True
                
    # Player hand creation module           
    deck.shuffle()
    for _ in range(2):
        for player in players:
              player.add_cards(deck.one_deal())
        dealer.add_cards(deck.one_deal())
        
    # Player hand displey module   
    for player in players:
        player.display()
        
    dealer.display()  
    
    # Player deal module
    for player in players:
        player.hand_values()
        if player.blackjack():
            print(f'{player.name}, you have a Black Jack!')
        else:
            while player.hand_values() <21:
                
                if game_play(player)==False:
                    break
                        
            else:
                if player.hand_values() !=21:
                    print('Bust!')
                    break
                    
    
    
    # Dealer Module
    
    
            
from IPython.display import clear_output

print('\t\tWelcome to Black Jack!\t\t')
num =0
players =[]
deck = Deck()
dealer = Dealer()
while num not in range(1,7):
    num = int(input('Please enter the number of players(1-6): '))

for n in range(1,num+1):
    name = input(f'Player {n} please enter your name: ').title()
    bankroll =0
    while bankroll not in range(100, 10001):
        bankroll = int(input(f'{name}, plese enter your bankroll(min $ 100; max $ 10000): '))
    players.append(Player(name, bankroll))


game_on = True
round =1
while game_on:
    print(f'Round {round}')
    one_round(players)
    dealer_func()
    for player in players:
        if player.bankroll >=10:
            reply =  ''
            while reply not in ['Yes', 'No', 'Y', 'N']:
                reply = input(f'{player.name}, do you wish to continue?(Y/N)').title()
            if reply in ['Yes', 'Y']:
                player.hand =[]
                deck =Deck()
                dealer =Dealer()
                continue
            else:
                print('Goodbye!')
                players.remove(player)
                
                
        else:
            print(f'{player.name} you dont have enough chips for another round!')
            players.remove(player)
    round +=1        
    if len(players)==0:
        game_on = False
    else:
        game_on=True
    clear_output()        
   