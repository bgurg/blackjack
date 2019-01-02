playing = True

import deck as deck
import bet as bet
import show_hands as show

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

		if (input('\nPress "h" to hit (any other key to stand): ').lower() == "h"):
			player_hand.add_card(game_deck.deal())
		else:
			stand = True

	if player_hand.busted():
		show.show_all(player_hand, dealer_hand, player_chips)
		player_chips.lose_bet()
		print(f'\nPlayer busts with {player_hand.value}')
		print(f'PLAYER LOSES...new chips total: {player_chips.total}')
	else:
		while not dealer_hand.busted() and (dealer_hand.value < player_hand.value):
			dealer_hand.add_card(game_deck.deal())

		show.show_all(player_hand, dealer_hand, player_chips)

		if dealer_hand.busted():
			player_chips.win_bet()
			print(f'\nDealer busts with {dealer_hand.value}')
			print(f'\nPLAYER WINS...new chips total: {player_chips.total}')
		else:
			player_chips.lose_bet()
			print(f'\nDealer wins with {dealer_hand.value}')
			print(f'PLAYER LOSES...new chips total: {player_chips.total}')

	if  player_chips.total == 0:
		print('Sorry but you are out of chips.')
		playing = False
	else:
		response = ''
		while response not in ['y','n']:
			response = input('Play again (y/n)? ').lower()
		playing = (response == 'y')
