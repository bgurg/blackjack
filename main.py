from colorama import Fore

playing = True

import deck as deck
import bet as bet
import show as show

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

		stand = show.hit_or_stand(game_deck, player_hand)

	if player_hand.busted():
		show.show_all(player_hand, dealer_hand, player_chips)
		show.dealer_wins(dealer_hand, player_chips)
	else:
		while not dealer_hand.busted() and (dealer_hand.value < player_hand.value):
			dealer_hand.add_card(game_deck.deal())

		show.show_all(player_hand, dealer_hand, player_chips)

		if dealer_hand.busted():
			show.player_wins(player_hand, player_chips)
		else:
			show.dealer_wins(dealer_hand, player_chips)
	
	playing = show.user_continue(player_chips)
