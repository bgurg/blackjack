import deck as deck
import show_hands as show

test_deck = deck.Deck()
test_deck.shuffle()

dealer = deck.Hand(test_deck)
player = deck.Hand(test_deck)

dealer.add_card(test_deck.deal())
dealer.add_card(test_deck.deal())
dealer.add_card(test_deck.deal())

player.add_card(test_deck.deal())
player.add_card(test_deck.deal())

show.show_some(player, dealer)
print('-'*25, '\n')
show.show_all(player, dealer)

