from classes import *
from classes import playing

while True:
    # Print an opening statement
    print('Welcome to BlackJack! Get as close to 21 as you can without going over!\n\
    Dealer hits until reaching 17. Aces count as 1 or 11.')

    new_deck = Deck()
    new_deck.shuffle()
    player_hand = Hand()
    player_hand.add_card(new_deck.deal_a_card())
    player_hand.add_card(new_deck.deal_a_card())

    dealer_hand = Hand()
    dealer_hand.add_card(new_deck.deal_a_card())
    dealer_hand.add_card(new_deck.deal_a_card())

    player_chips = Chips()
    place_a_bet(player_chips)
    show_some(player_hand, dealer_hand)

    while playing:

        # Prompt for Player to Hit or Stand
        hit_or_stand(new_deck, player_hand)

    # Show cards (but keep one dealer card hidden)
        show_some(player_hand, dealer_hand)

    # If player's hand exceeds 21, run player_busts() and break out of loop
        if player_hand.value > 21:
            player_busts(player_hand, dealer_hand, player_chips)
            break

        # If Player hasn't busted, play Dealer's hand until Dealer reaches 17
        if player_hand.value <= 21:
            while dealer_hand.value < 17:
                hit(new_deck, dealer_hand)

        # Show all cards
        show_all(player_hand, dealer_hand)

    # Run different winning scenarios
        if dealer_hand.value > 21:
            dealer_busts(player_hand, dealer_hand, player_chips)
            break

        elif dealer_hand.value > player_hand.value:
            dealer_wins(player_hand, dealer_hand, player_chips)
            break

        elif dealer_hand.value < player_hand.value:
            player_wins(player_hand, dealer_hand, player_chips)
            break

        else:
            push(player_hand, dealer_hand)

        # Inform Player of their chips total
    print("\nPlayer's winnings stand at", player_chips.total)

# Ask to play again
    new_game = input("Would you like to play another hand? Enter 'y' or 'n' ")

    if new_game[0].lower() == 'y':
        playing = True
        continue
    else:
        print("Thanks for playing!")
        break
