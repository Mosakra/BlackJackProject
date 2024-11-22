import random

# suits, ranks, and point values
def create_deck():
    suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    points = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10,
              'J': 10, 'Q': 10, 'K': 10, 'A': 11} 
    deck = [[suit, rank, points[rank]] for suit in suits for rank in ranks]
    player_hand = []
    dealer_hand = []
    print(deck)

def main():
    print("BLACKJACK!")
    print("Blackjack payout is 3:2")
    create_deck()
    
    







if __name__ == "__main__":
    main()