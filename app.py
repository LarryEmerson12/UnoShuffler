import random

deck = []
colors = ['🔴', '🟡', '🟢', '🔵']
cards = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 'Draw Two', 'Skip', 'Reverse']
wilds = ['Wild', 'Wild Draw Four']

"""
Generates the Uno cards.
"""
def generateDeck():
  for color in colors:
    for card in cards:
      cardVal = '{} {}'.format(color, card)
      deck.append(cardVal)
      if card != 0:
        if card != 'Draw Two':
          if card != 'Skip':
            if card != 'Reverse':
              deck.append(cardVal)
  for wild in wilds:
    for i in range(2):
      deck.append(wild)

def shuffleDeck():
  random.shuffle(deck)

def display(deck):
  for i in deck:
    print(i)

generateDeck()
shuffleDeck()

print(deck)

# If you want to print the deck one-by-one, use display(deck).
# display(deck)