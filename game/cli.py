from game.deck import Deck

deck = Deck()
deck.shuffle()

card = deck.deal()
print(card)