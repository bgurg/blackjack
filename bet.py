from clear import clear

class Chips:
    def __init__(self, total):
        self.total = total
        self.bet = 0

    def __str__(self):
        return 'Currently betting ' + str(self.bet) + ' of ' + str(self.total) + ' chips'

    def win_bet(self):
        self.total += self.bet
        self.bet = 0

    def lose_bet(self):
        self.total -= self.bet
        self.bet = 0

#-----------------------------------------------------

def take_bet(chips):
    clear()
    print(chips)

    valid_bet = False

    while not valid_bet:
        try:
            amt = int(input('Enter bet: '))
        except:
            print('Invalid entry.  Bet amount must be an integer.')
            amt = ''

        if type(amt) == int:
            if amt > chips.total:
                print(f'Insufficient chips.  You only have {chips.total} chips to bet.')
            else:
                chips.bet = amt
                valid_bet = True
