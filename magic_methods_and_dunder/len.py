class DeckOfCards:
    def __init__(self):
        # Initialize a standard deck of 52 playing cards
        ranks = ['2', '3', '4', '5', '6', '7',
                 '8', '9', '10', 'J', 'Q', 'K', 'A']
        suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        self.cards = [(rank, suit) for rank in ranks for suit in suits]

    def __len__(self):
        # Return the number of cards in the deck
        return len(self.cards)


# Create an instance of DeckOfCards
deck = DeckOfCards()

# Use len() to get the number of cards in the deck
num_of_cards = len(deck)
print(f"Number of cards in the deck: {num_of_cards}")
