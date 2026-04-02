from game.deck import Deck
from game.player import Player


class Game:
    def __init__(self, player_names):
        self.players = [Player(name, 1000) for name in player_names]
        self.deck = Deck()
        self.community_cards = []
        self.pot = 0
        self.stage = "pre-flop"  # game state to track where one is in the game

    def reset_round(self):
        print("\n--- Reseting the Round ---")

        self.deck = Deck()
        self.deck.shuffle()
        self.community_cards = []
        self.stage ="pre-flop"

        for player in self.players:
            player.clear_hand()

    def start(self):
        self,self.reset_round()

        print("Starting game...")

        self.deal_to_players()

    def deal_to_players(self):
        for _ in range(2):  # each player gets 2 cards
            for player in self.players:
                card = self.deck.deal()
                player.receive_card(card)

    def deal_flop(self):
        print("\nDealing Flop...")
        for _ in range(3):
            card = self.deck.deal()
            self.community_cards.append(card)
        self.stage = "flop"

    def deal_turn(self):
        print("\nDealing Turn...")
        card = self.deck.deal()
        self.community_cards.append(card)
        self.stage = "turn"

    def deal_river(self):
         print("\nDealing River...")
         card = self.deck.deal()
         self.community_cards.append(card)
         self.stage = "river"

    def show_players_hands(self):
        print("\nPlayer Hands;")
        for player in self.players:
            print(f"{player.name}: {player.show_hand()}")

    def show_community_cards(self):
        print("\nCommunity Cards:")
        print(", ".join(str(card) for card in self.community_cards))