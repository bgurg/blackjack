import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')

ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')

values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10,
         'Queen':10, 'King':10, 'Ace':11}

#-----------------------------------------------------

class Card():
    
    def __init__(self, rank, suit):
        self.suit = suit
        self.rank = rank
        self.is_ace = (rank == 'Ace')
    
    def __str__(self):
        return self.rank + " of " + self.suit

#-----------------------------------------------------

class Deck():
    
    def __init__(self):
        self.deck = []  # start with an empty list
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(rank, suit))
    
    def __len__(self):
        return len(self.deck)
    
    def __str__(self):
        deck_str = ''
        for card in self.deck:
            deck_str += card.__str__() + ' (' + str(values[card.rank]) + ')\n' 
        return deck_str

    def shuffle(self):
        random.shuffle(self.deck)
        
    def deal(self):
        dealt_card = self.deck.pop()
        return dealt_card

#-----------------------------------------------------

class Hand:
    def __init__(self, deck):
        self.cards = []  # start with an empty list as we did in the Deck class
        self.value = 0   # start with zero value
        self.non_adjusted_aces = 0
        self.add_card(deck.deal())
        self.add_card(deck.deal())

    def __str__(self):
        hand_str = ''
        for card in self.cards:
            hand_str += card.__str__() + ' (' + str(values[card.rank]) + ')\n' 
        hand_str += 'Hand value = ' + str(self.value)
        return hand_str
        
    def add_card(self,card):
        self.cards.append(card)
        self.value += values[card.rank]
        
        if card.is_ace:
            self.non_adjusted_aces += 1

        if self.value > 21:
            self.adjust_aces()
            
    def adjust_aces(self):
        for i in range(0,self.non_adjusted_aces):
            if self.value > 21:
                self.value -= 10
                self.non_adjusted_aces -= 1
                print(f'adjusted value = {self.value} ... remaining aces = {self.non_adjusted_aces}')

    def busted(self):
        return self.value > 21
