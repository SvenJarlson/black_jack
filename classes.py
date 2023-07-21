import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8, 'Nine': 9, 'Ten': 10,
          'Jack': 10, 'Queen': 10, 'King': 10, 'Ace': 11}

playing = True


class Card:

    def __init__(self, suit, rank):
        self.suit = suit.capitalize()
        self.rank = rank.capitalize()
        self.value = values[self.rank]

    def __str__(self):
        return self.rank + " of " + self.suit


class Deck:

    def __init__(self):

        self.deck = []

        for suit in suits:
            for rank in ranks:
                # create an object Card
                created_card = Card(suit, rank)

                self.deck.append(created_card)

    def shuffle(self):

        random.shuffle(self.deck)

    def deal_a_card(self):
        single_card = self.deck.pop()
        return single_card


class Player:

    def __init__(self, name):
        self.name = name
        self.all_cards = []

    def __str__(self):
        return f'Player {self.name}, you have {self.all_cards}'


class Hand:
    def __init__(self):
        self.cards = []  # start with an empty list as we did in the Deck class
        self.value = 0  # start with zero value
        self.aces = 0  # add an attribute to keep track of aces

    def add_card(self, card):
        self.cards.append(card)
        self.value += values[card.rank]
        if card.rank == 'Ace':
            self.aces += 1

    def adjust_for_ace(self):
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1


class Chips:

    def __init__(self):
        self.total = 100
        self.bet = 0

    def win_bet(self):
        self.total += self.bet

    def lose_bet(self):
        self.total -= self.bet


def place_a_bet(chips):
    while True:
        try:
            chips.bet = int(input("How much would you like to bet? "))
        except ValueError:
            print("That is not a valid number.")
            continue
        else:
            if chips.bet > chips.total:
                print("Your bet exceeds your chips. You're broken, dude. Go home.", chips.total)
            else:
                break


def hit(deck, hand):
    hand.add_card(deck.deal_a_card())
    hand.adjust_for_ace()


def hit_or_stand(deck, hand):
    global playing
    # to control an upcoming while loop

    while True:
        x = input("Would you like to Hit or Stand? Enter 'h' or 's' ")

        if x[0].lower() == 'h':
            hit(deck, hand)  # hit() function defined above

        elif x[0].lower() == 's':
            print("Player stands. Dealer is playing.")
            playing = False

        else:
            print("That is not a valid answer.")
            continue
        break


def show_some(player, dealer):
    print("\nDealer's Hand:")
    print(" <card hidden>")
    print('', dealer.cards[1])
    print("\nPlayer's Hand:", *player.cards, sep='\n ')


def show_all(player, dealer):
    print("\nDealer's Hand:", *dealer.cards, sep='\n ')
    print("Dealer's Hand =", dealer.value)
    print("\nPlayer's Hand:", *player.cards, sep='\n ')
    print("Player's Hand =", player.value)


def player_busts(player, dealer, chips):
    print("Player busts!")
    chips.lose_bet()


def player_wins(player, dealer, chips):
    print("Player wins!")
    chips.win_bet()


def dealer_busts(player, dealer, chips):
    print("Dealer busts!")
    chips.win_bet()


def dealer_wins(player, dealer, chips):
    print("Dealer wins!")
    chips.lose_bet()


def push(player, dealer):
    print("Dealer and Player tie! It's a push.")
