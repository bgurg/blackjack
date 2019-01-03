from colorama import Fore

playing = True

import deck as deck
import bet as bet
import show as show

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
    print(Fore.YELLOW)
    print(f'\nDealer wins with {hand.value}')
    print(Fore.WHITE)
    print(f'New chips total: {chips.total}  ', end='')

#-----------------------------------------------------

def player_wins(hand, chips):
    chips.win_bet()
    print(Fore.CYAN)
    print(f'\nPlayer wins with {hand.value}')
    print(Fore.WHITE)
    print(f'\nNew chips total: {chips.total}  ', end='')

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

#-----------------------------------------------------

player_chips = bet.Chips(100)

while playing:
	game_deck = deck.Deck()
	game_deck.shuffle()

	player_hand = deck.Hand(game_deck)
	dealer_hand = deck.Hand(game_deck)

	bet.take_bet(player_chips)

	stand = False
	while not player_hand.busted() and not stand:
		show.show_some(player_hand, dealer_hand, player_chips)

		stand = hit_or_stand(game_deck, player_hand)

	if player_hand.busted():
		show.show_all(player_hand, dealer_hand, player_chips)
		dealer_wins(dealer_hand, player_chips)
	else:
		while not dealer_hand.busted() and (dealer_hand.value < player_hand.value):
			dealer_hand.add_card(game_deck.deal())

		show.show_all(player_hand, dealer_hand, player_chips)

		if dealer_hand.busted():
			player_wins(player_hand, player_chips)
		else:
			dealer_wins(dealer_hand, player_chips)
	
	playing = user_continue(player_chips)
