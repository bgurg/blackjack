from colorama import Fore

INDENT = 5

def show_some(player,dealer,chips):

    print('\n'*50)
    print(chips)
    print('\n')

    print(Fore.YELLOW)
    print(f'Dealer showing:')
    
    dealer_tmp = []
    for card in dealer.cards:
        dealer_tmp.append(card)

    dealer_tmp.pop(0)

    print(' '*INDENT, end='')
    print('CARD FACEDOWN')

    for card in dealer_tmp:
        print(' '*INDENT, end='')
        print(card)
    print()

    print(Fore.CYAN)
    print(f'Player at {player.value} with:')
    for card in player.cards:
        print(' '*5, end='')
        print(card)
    
#-----------------------------------------------------

def show_all(player,dealer,chips):

    print('\n'*50)
    print(chips)
    print('\n')

    print(Fore.YELLOW)
    print(f'Dealer at {dealer.value} with:')

    for card in dealer.cards:
        print(' '*INDENT, end='')
        print(card)
    print()

    print(Fore.CYAN)
    print(f'Player at {player.value} with:')
    for card in player.cards:
        print(' '*INDENT, end='')
        print(card)
    
