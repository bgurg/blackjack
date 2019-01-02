import bet as bet

x = bet.Chips(100)
print(x)

bet.take_bet(x)
print(x)

print('win')
x.win_bet()
print(x)

bet.take_bet(x)
print(x)

print('lose')
x.lose_bet()
print(x)

