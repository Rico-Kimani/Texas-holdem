from game.game import Game


def main():
    game = Game(["Erick", "Alice"])

    game.start()
    game.show_players_hands()

    # ---------------- PRE-FLOP ----------------
    game.betting_round()
    if len(game.active_players()) == 1:
        game.determine_winner()
        return

    # ---------------- FLOP ----------------
    game.deal_flop()
    game.show_community_cards()

    game.betting_round()
    if len(game.active_players()) == 1:
        game.determine_winner()
        return

    # ---------------- TURN ----------------
    game.deal_turn()
    game.show_community_cards()

    game.betting_round()
    if len(game.active_players()) == 1:
        game.determine_winner()
        return

    # ---------------- RIVER ----------------
    game.deal_river()
    game.show_community_cards()

    game.betting_round()
    if len(game.active_players()) == 1:
        game.determine_winner()
        return

    # ---------------- SHOWDOWN ----------------
    game.determine_winner()


if __name__ == "__main__":
    main()