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


    def get_card_value(self, card):
         values = {
             "2": 2, "3": 3, "4": 4, "5": 5,
             "6": 6, "7": 7, "8": 8, "9": 9,
             "10": 10, "J": 11, "Q": 12,
             "K": 13, "A": 14
    }
         return values[card.rank]
    

    def get_best_card(self, player):
        all_cards = player.hand + self.community_cards
        return max(all_cards, key=self.get_card_value)
    
    def determine_winner(self):
        print("\n--- Determining Winner ---")

        best_player = None
        best_card = None

        for player in self.players:
            player_best = self.get_best_card(player)
            print(f"{player.name}'s best card: {player_best}")


            if best_card is None or self.get_card_value(player_best) > self.get_card_value(best_card):
                best_card = player_best
                best_player = player

        print(f"\nWinner: {best_player.name} with {best_card}")