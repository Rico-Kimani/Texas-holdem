class Player:
    def __init__(self, name, chips):
        self.name = name
        self.chips = chips
        self.hand = []   

    def receive_card(self, card):
        self.hand.append(card)

    def clear_hand(self):
        self.hand = []

    def show_hand(self):
        return ", ".join(str(card) for card in self.hand)

    def bet(self, amount):
        if amount > self.chips:
            print(f"{self.name} does not have enough chips!")
            return 0
        self.chips -= amount
        return amount