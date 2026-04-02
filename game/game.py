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
        print("\n--- Resetting the Round ---")

        self.deck = Deck()
        self.deck.shuffle()
        self.community_cards = []
        self.pot = 0
        self.stage ="pre-flop"

        for player in self.players:
            player.clear_hand()

    def start(self):
        self.reset_round()

        print("Starting game...")

        self.deal_to_players()

    def deal_to_players(self):
        for _ in range(2):  # each player gets 2 cards
            for player in self.players:
                player.receive_card(self.deck.deal())

    def deal_flop(self):
        print("\nDealing Flop...")
        for _ in range(3):
            self.community_cards.append(self.deck.deal())
        self.stage = "flop"

    def deal_turn(self):
        print("\nDealing Turn...")
        self.community_cards.append(self.deck.deal())
        self.stage = "turn"

    def deal_river(self):
         print("\nDealing River...")
         self.community_cards.append(self.deck.deal())
         self.stage = "river"

    def show_players_hands(self):
        print("\nPlayer Hands:")
        for player in self.players:
            if not player.folded:
               print(f"{player.name}: {player.show_hand()}")

    def show_community_cards(self):
        print("\nCommunity Cards:")
        print(", ".join(str(card) for card in self.community_cards))

    def active_players(self):
        return [player for player in self.players if not player.folded]
    
        #Bet System
    def betting_round(self):
        print("\n--- Betting Round ---")

        for player in self.players:
            if player.folded:
                continue
           

           #Stops if one player left
            if len(self.active_players()) <=1:
                return

            print(f"\n{player.name}'s turn (Chips: {player.chips})")
            action = input("Choose action (bet/check/fold): ").lower()

            if action == "bet":
                amount = int(input("Enter bet amount: "))
                bet = player.bet(amount)
                self.pot += bet

            elif action == "fold":
                player.fold()
                print(f"{player.name} folds.")

            else:
                print(f"{player.name} checks.")

        print(f"\nTotal Pot: {self.pot}")

    def get_card_value(self, rank):
         values = {
             "2": 2, "3": 3, "4": 4, "5": 5,
             "6": 6, "7": 7, "8": 8, "9": 9,
             "10": 10, "J": 11, "Q": 12,
             "K": 13, "A": 14
    }
         return values[rank]
    
    def get_rank_counts(self, cards):
        counts = {}
        for card in cards:
            counts[card.rank] = counts.get(card.rank, 0) + 1
        return counts
    
    def get_pair(self, cards):
        counts = self.get_rank_counts(cards)
        pairs = [rank for rank, count in counts.items() if count == 2]

        if pairs:
            return max(pairs, key=self.get_card_value)
        return None


    def get_best_card(self, cards):
        return max(cards, key=lambda c: self.get_card_value(c.rank))
    
    def evaluate_hand(self, player):
        cards = player.hand + self.community_cards

        pair = self.get_pair(cards)
        if pair:
            return(2,pair)
        best = self.get_best_card(cards)
        return (1, best.rank)
    

    def compare_scores(self, s1, s2):
        if s1[0] != s2[0]:
            return s1[0] > s2[0]
        return self.get_card_value(s1[1]) > self.get_card_value(s2[1])
    
    def determine_winner(self):
        print("\n--- Determining Winner ---")
        
        active_players = [p for p in self.players if not p.folded]

        #  Everyone folded
        if len(active_players) == 0:
            print("All players folded. No winner.")
            return

         # Only one player left → auto win
        if len(active_players) == 1:
            winner = active_players[0]
            print(f"\n🏆 {winner.name} wins (everyone else folded)!")
            winner.chips += self.pot
            return

        # Normal comparison
        best_player = None
        best_score = None

        for player in active_players:
            score = self.evaluate_hand(player)
            
            if score[0] == 2:
                print(f"{player.name} has a PAIR of {score[1]}'s")
            else:
                print(f"{player.name} has HIGH CARD {score[1]}")

            if best_score is None or self.compare_scores(score, best_score):
                best_score = score
                best_player = player
                
        print(f"\n🏆 Winner: {best_player.name} wins {self.pot} chips!")
        best_player.chips += self.pot