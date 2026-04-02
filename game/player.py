class Player:
    def __init__(self, name, chips):
        self.name = name
        self.chips = chips
        self.hand = []   
        self.current_bet = 0
        self.olded = False

    def receive_card(self, card):
        self.hand.append(card)

    def clear_hand(self):
        self.hand = []
        self.current_bet = 0
        self.folded = False

    def show_hand(self):
        return ", ".join(str(card) for card in self.hand)

    def bet(self, amount):
        if amount > self.chips:
            print(f"{self.name} does not have enough chips!")
            return 0
        
        self.chips -= amount
        self.current_bet += amount
        return amount
    
    def fold(self):
        self.folded = True