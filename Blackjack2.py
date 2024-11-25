import random



# bet amount / money total



def shuffle_deck(deck):
    random.shuffle(deck)



# Deck of cards / player dealers hands
deck = []
player_hand = []
dealer_hand = []

# deal the cards
def deal_hand(deck):
    return [deck.pop(), deck.pop()]


# Calculate the total of each hand
total = sum([card [2] for card in hand if card[1] != "Ace"])
aces = [card for card in hand if card[1] == "Ace"]

# check for winner




# game loop


def main():
    print("BLACKJACK!")
    print("Blackjack payout is 3:2")








if __name__ == "__main__":
    main()