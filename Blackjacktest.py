import random

suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
values = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 10, 'Q': 10, 'K': 10, 'A': 11}

def create_deck():
    deck = []
    for suit in suits:
        for rank in ranks:
            deck.append([rank, suit, values[rank]])
    return deck

def calculate_hand_value(hand):
    value = sum(card[2] for card in hand)
    aces = sum(1 for card in hand if card[0] == 'A')
    while value > 21 and aces:
        value -= 10
        aces -= 1
    return value

def print_hand(name, hand, hide_first_card=False):
    # If we want to hide the first card (like the dealer's show card)
    if hide_first_card:
        print(f"{name}'s Cards: {hand[0][0]} of {hand[0][1]}, ?")
    else:
        # Print each card on a new line
        print(f"{name}'s Cards:")
        for card in hand:
            print(f"{card[0]} of {card[1]}")
    print()  # Add a blank line after the cards

def dealer_play(deck, dealer_hand):
    while calculate_hand_value(dealer_hand) < 17:
        dealer_hand.append(deck.pop())
        print_hand("Dealer", dealer_hand)
    return calculate_hand_value(dealer_hand)

def main():
    print("BLACKJACK!")
    print("Blackjack payout is 3:2\n")
    deck = create_deck()
    player_bust = False
    dealer_bust = False

    while True:
        random.shuffle(deck)
        player_hand = []
        dealer_hand = []
        player_bust = False
        dealer_bust = False

        # Deal initial cards
        for _ in range(2):
            player_hand.append(deck.pop())
            dealer_hand.append(deck.pop())

        # Display dealer's show card (hide the second card for now)
        print(f"DEALER'S SHOW CARD:")
        print(f"{dealer_hand[0][0]} of {dealer_hand[0][1]}")
        print()  # Blank line for clarity
        
        # Display player's cards (all cards visible)
        print_hand("\nYOUR CARDS:", player_hand)

        # Player's turn
        while not player_bust:
            player_value = calculate_hand_value(player_hand)
            if player_value > 21:
                print("Player busts! You lose!")
                player_bust = True
                break

            action = input("Hit or stand? (hit/stand): ").lower()
            if action == 'hit':
                player_hand.append(deck.pop())
                print_hand("\nYOUR CARDS:", player_hand)
            elif action == 'stand':
                break
            else:
                print("Invalid choice. Please enter 'hit' or 'stand'.")

        # If player hasn't bust, dealer plays
        if not player_bust:
            dealer_value = dealer_play(deck, dealer_hand)

            # Print dealer's full hand after playing
            print_hand("Dealer", dealer_hand, hide_first_card=False)

            if dealer_value > 21:
                print("Dealer Busts! You Win!")
                dealer_bust = True
        # display player's and dealer's values
        player_value = calculate_hand_value(player_hand)
        dealer_value = calculate_hand_value(dealer_hand)
        print()
        print(f"YOUR POINTS:     {player_value}")
        print(f"DEALER'S POINTS: {dealer_value}")

        # Determine the winner if the game is over
        if player_bust:
            print()
            print("Sorry. You lose.")
        elif dealer_bust:
            print()
            print("Dealer loses.")
        else:
            player_value = calculate_hand_value(player_hand)
            if player_value > dealer_value:
                print()
                print("Player wins!")
            elif player_value < dealer_value:
                print()
                print("Dealer wins!")
            else:
                print()
                print("It's a tie!")

        # Ask to play again
        play_again = input("\nPlay again? (y/n)").lower()
        if play_again != 'y':
            print("\nCome back soon!")
            break
    print("Bye!")

if __name__ == "__main__":
    main()

            

