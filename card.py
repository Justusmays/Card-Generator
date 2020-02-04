import random

symbols = ['\u2665', '\u2666', '\u2660', '\u2663']
number = ['A',2,3,4,5,6,7,8,9,10, 'J', 'Q', 'K']

random_symbol = random.choice(symbols)
random_number = random.choice(number)
print(random_symbol,random_number)
