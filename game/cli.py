from game.game import Game

game = Game(["Erick", "Alice"])

game.start()
game.show_players_hands()

game.deal_flop()
game.show_community_cards()

game.deal_turn()
game.show_community_cards()

game.deal_river()
game.show_community_cards()

game.determine_winner()
