"""
Spades Bot:
Rules:
Each player (4 players is standard) is dealt 13 cards at random.
Before the game begins there is a round of bidding which I will explain later.
The goal of the game is to obtain the most points.
A game of spades generally consists of multiple hands.
Each hand, a "lead card" is played, and each of the players in clockwise order
must play a card that follows suit. If a player does not have a card that
matches suit, then they can either play another suit, besides spades, that will
have no value, or they could play a spade which "trumps" the hand. If multiple
spades are played in one hand, the highest one wins the hand. The winner of the
hand is the player who has the highest card that matches the suit of the lead
card or the highest spade. Before each hand, the players will go around,
beginning with the player left of the dealer and continuing clockwise, and
will bid how many hands they think they will recieve. The closer a player is to
their bid, the more points they will recieve.

Scoring:
"Underbid" -- A player is underbid when their bid is lower than the number of "tricks"
they won. The score for an underbid player is 10 * their bid plus one point for
each additional bid. For instance, if a player bid 3 and got 4, they would get
30 (10 * 3), plus 1 (one extra), or 31.

"Well Bid" -- A player is well bid when their bid is equal to the number of tricks
they won. The score for a well bid player is 10 * their bid + 30 points. For instance,
if a player bid 3 and got 3, they would get 30 (10 * 3) + 30 (well bid bonus), or 60.

"Overbid" -- A player is overbid when their bid is higher than the number of tricks
they won. The score for an overbid player is 10 * the number of tricks they got,
minus 10 for each trick they did not get below their bid. For instance, if a player
bid 4 and got three, they would get 30 (10 * 3) minus 10 (10 * number of tricks they
didn't get), or 20.

"""
import random

# Spades = 4, Hearts = 3, Diamonds = 2, and Clubs = 1
class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value
        self.suitName = None
        if suit == 1:
            self.suitName = 'Clubs'
        elif suit == 2:
            self.suitName = 'Diamonds'
        elif suit == 3:
            self.suitName = 'Hearts'
        elif suit == 4:
            self.suitName = 'Spades'
    def value_name(self, value):
        return {
            2: 'Two',
            3: 'Three',
            4: 'Four',
            5: 'Five',
            6: 'Six',
            7: 'Seven',
            8: 'Eight',
            9: 'Nine',
            10: 'Ten',
            11: 'Jack',
            12: 'Queen',
            13: 'King',
            14: 'Ace',
        }.get(value)

class Game:
    def __init__(self):
        self.cardList = [] # temporary list to store card objects
        self.cards = 52 # standard playing card deck
        self.players = 4 # number of players in the game
        self.tricks = 52 // self.players # round down number of hands

        self.player1 = [] # Each player will be a list of cards
        self.player2 = [] # then we will use sorting and ranking to decide which
        self.player3 = [] # player will bid what and which card should be played
        self.player4 = [] # this __init__ and Deal are just setup methods.
        self.playerList = [self.player1, self.player2, self.player3, self.player4]
    def pop_deck(self): # method for creating the deck
        for j in range(2, 15): # for each
            for i in range(1, 5):
                self.cardList.append(Card(i, j))
    def deal(self):
        for j in self.playerList:
            for i in range(13):
                card = random.choice(self.cardList)
                j.append(card)
                self.cardList.remove(card)
class Player(Game):
    def __init__(self, cards):
        self.cards = cards
        self.handvalues = []
        self.bid = 0
    def get_values(self):
        for i in range(13):
            self.handvalues.append([self.cards[i].suit, self.cards[i].value])
        self.handvalues = sorted(self.handvalues, key=lambda x: (x[0], x[1]))
        #sort by suit, then rank
    def bid_logic(self):
        gen = (x for x in self.handvalues if (x[0]==4 and x[1]>=10)) # iterate
        #through spades higher than or equal to 10
        for x in gen:
            self.bid = self.bid + 1


test = Game()
test.pop_deck()
test.Deal()
player1 = Player(test.player1)
player1.getValues()
player1.bidLogic()
print player1.bid
print player1.handvalues
