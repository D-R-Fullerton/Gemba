import tkinter as tk
import random

class BlackjackGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Blackjack")

        self.deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11] * 4
        random.shuffle(self.deck)

        self.player_hand = []
        self.dealer_hand = []
        self.split_hand = []

        self.status = tk.Label(self.root, text="Welcome to Blackjack", font=('Helvetica', 14))
        self.status.pack()

        self.player_label = tk.Label(root, text="Your Hand:")
        self.player_label.pack()

        self.dealer_label = tk.Label(root, text="Dealer's Hand:")
        self.dealer_label.pack()

        self.hit_button = tk.Button(root, text="Hit", command=self.hit)
        self.hit_button.pack(side="left")

        self.stand_button = tk.Button(root, text="Stand", command=self.stand)
        self.stand_button.pack(side="left")

        self.split_button = tk.Button(root, text="Split", command=self.split)
        self.split_button.pack(side="left")

        self.deal()

    def deal_card(self):
        return self.deck.pop()

    def score(self, hand):
        s = sum(hand)
        if s > 21 and 11 in hand:
            hand[hand.index(11)] = 1
        return sum(hand)

    def deal(self):
        self.player_hand = [self.deal_card(), self.deal_card()]
        self.dealer_hand = [self.deal_card(), self.deal_card()]
        self.update_labels()

    def update_labels(self):
        self.player_label.config(text=f"Your Hand: {self.player_hand} (Score: {self.score(self.player_hand)})")
        self.dealer_label.config(text=f"Dealer's Hand: [{self.dealer_hand[0]}, ?]")

        if len(set(self.player_hand)) == 1:
            self.split_button.config(state="normal")
        else:
            self.split_button.config(state="disabled")

    def hit(self):
        self.player_hand.append(self.deal_card())
        self.update_labels()
        if self.score(self.player_hand) > 21:
            self.status.config(text="Busted! Dealer wins.")

    def stand(self):
        while self.score(self.dealer_hand) < 17:
            self.dealer_hand.append(self.deal_card())
        self.update_labels()
        dealer_score = self.score(self.dealer_hand)
        player_score = self.score(self.player_hand)

        if dealer_score > 21 or player_score > dealer_score:
            self.status.config(text="You win!")
        elif player_score < dealer_score:
            self.status.config(text="Dealer wins!")
        else:
            self.status.config(text="Draw!")

    def split(self):
        # Split logic here: move one card to a new hand and play both
        self.status.config(text="Split feature coming soon... 🎭")

root = tk.Tk()
game = BlackjackGUI(root)
root.mainloop()
