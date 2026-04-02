from game.game import Game


def print_divider():
    print("\n" + "=" * 40)


def main():
    print_divider()
    print("🃏 TEXAS HOLD'EM (CLI VERSION)")
    print_divider()

    game = Game(["Erick", "Alice"])

    game.start()

    print_divider()
    print("🎴 Player Hands")
    game.show_players_hands()

    # ---------------- PRE-FLOP ----------------
    print_divider()
    print("💰 Pre-Flop Betting")
    game.betting_round()

    if len(game.active_players()) == 1:
        game.determine_winner()
        return

    # ---------------- FLOP ----------------
    print_divider()
    print("🂡 Flop")
    game.deal_flop()
    game.show_community_cards()

    print_divider()
    print("💰 Betting Round")
    game.betting_round()

    if len(game.active_players()) == 1:
        game.determine_winner()
        return

    # ---------------- TURN ----------------
    print_divider()
    print("🂱 Turn")
    game.deal_turn()
    game.show_community_cards()

    print_divider()
    print("💰 Betting Round")
    game.betting_round()

    if len(game.active_players()) == 1:
        game.determine_winner()
        return

    # ---------------- RIVER ----------------
    print_divider()
    print("🂮 River")
    game.deal_river()
    game.show_community_cards()

    print_divider()
    print("💰 Final Betting")
    game.betting_round()

    if len(game.active_players()) == 1:
        game.determine_winner()
        return

    # ---------------- SHOWDOWN ----------------
    print_divider()
    print("🏁 Showdown")
    game.determine_winner()
    print_divider()


if __name__ == "__main__":
    main()