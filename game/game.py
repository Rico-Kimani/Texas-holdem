from game.deck import Deck
from game.player import Player


class Game:
    def __init__(self, player_names):
        self.players = [Player(name, 1000) for name in player_names]
        self.deck = Deck()
        self.community_cards = []
        self.pot = 0
        self.stage = "pre-flop"  # game state to track where one is in the game

    def start(self):
        print("Starting game...")

        self.deck.shuffle()
        self.deal_to_players()

    def deal_to_players(self):
        for _ in range(2):  # each player gets 2 cards
            for player in self.players:
                card = self.deck.deal()
                player.receive_card(card)

    def show_players_hands(self):
        for player in self.players:
            print(f"{player.name}: {player.show_hand()}")