from colorama import Fore

def show_some(player,dealer,chips):

    print('\n'*50, chips, '\n')

    print(Fore.YELLOW, 'Dealer showing:')

    dealer_tmp = []
    for card in dealer.cards:
        dealer_tmp.append(card)

    dealer_tmp.pop(0)

    print('\t', 'CARD FACEDOWN')

    for card in dealer_tmp:
        print('\t', card)

    print('\n', Fore.CYAN, f'Player at {player.value} with:')
    for card in player.cards:
        print('\t', card)
    
#-----------------------------------------------------

def show_all(player,dealer,chips):

    print('\n'*50, chips, '\n')

    print(Fore.YELLOW, f'Dealer at {dealer.value} with:')

    for card in dealer.cards:
        print('\t', card)

    print('\n', Fore.CYAN, f'Player at {player.value} with:')
    for card in player.cards:
        print('\t', card)
    
#-----------------------------------------------------

def hit_or_stand(deck, hand):
    print(Fore.WHITE)
    if (input('\nPress "h" to hit (any other key to stand): ').lower() == "h"):
        hand.add_card(deck.deal())
        return False
    else:
        return True

#-----------------------------------------------------

def dealer_wins(hand, chips):
    chips.lose_bet()
    print(Fore.YELLOW, f'\nDealer wins with {hand.value}')
    print(Fore.WHITE, f'\nNew chips total: {chips.total}', end='')

#-----------------------------------------------------

def player_wins(hand, chips):
    chips.win_bet()
    print(Fore.CYAN, f'\nPlayer wins with {hand.value}')
    print(Fore.WHITE, f'\nNew chips total: {chips.total}', end='')

#-----------------------------------------------------

def user_continue(chips):
    print(Fore.WHITE)
    if  chips.total == 0:
        print('Sorry but you are out of chips.')
        return False
    else:
        response = ''
        while response not in ['y','n']:
            response = input('Would you like to play again (y/n)? ').lower()
        return (response == 'y')

