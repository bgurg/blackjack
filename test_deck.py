import deck as deck

test_deck = deck.Deck()
test_deck.shuffle()

p1 = deck.Hand(test_deck)

for i in range(0,3):
    p1.add_card(test_deck.deal())
    
print(p1)  
print(f'busted = {p1.busted()}')  

print(f'cards remaining in deck = {len(test_deck)}')
