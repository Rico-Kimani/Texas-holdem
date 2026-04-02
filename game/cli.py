from game.deck import Deck
from game.player import Player

deck = Deck()
deck.shuffle()

player = Player("Erick", 1000)

# Deal 2 cards
for _ in range(2):
    player.receive_card(deck.deal())

print(f"{player.name}'s hand:")
print(player.show_hand())