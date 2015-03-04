# Mini-project #6 - Blackjack

import simplegui
import random

# load card sprite - 936x384 - source: jfitz.com
CARD_SIZE = (72, 96)
CARD_CENTER = (36, 48)
card_images = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/cards_jfitz.png")

CARD_BACK_SIZE = (72, 96)
CARD_BACK_CENTER = (36, 48)
card_back = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/card_jfitz_back.png")    

# initialize some useful global variables
CANVAS_WIDTH = 600
CANVAS_HEIGHT = 600
CW_HALF = CANVAS_WIDTH / 2
CH_HALF = CANVAS_HEIGHT / 2
in_play = False
outcome = ""
score = [0, 0]
wins = score[0]
loss = score[1]

# define globals for cards
SUITS = ('C', 'S', 'H', 'D')
RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K')
VALUES = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':10, 'Q':10, 'K':10}


# define card class
class Card:
    def __init__(self, suit, rank):
        if (suit in SUITS) and (rank in RANKS):
            self.suit = suit
            self.rank = rank
        else:
            self.suit = None
            self.rank = None
            print "Invalid card: ", suit, rank

    def __str__(self):
        return self.suit + self.rank

    def get_suit(self):
        return self.suit

    def get_rank(self):
        return self.rank

    def draw(self, canvas, pos):
        card_loc = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS.index(self.rank), 
                    CARD_CENTER[1] + CARD_SIZE[1] * SUITS.index(self.suit))
        canvas.draw_image(card_images, card_loc, CARD_SIZE, [pos[0] + CARD_CENTER[0], pos[1] + CARD_CENTER[1]], CARD_SIZE)
    if in_play == True:
        card_loc = (CARD_CENTER[0], CARD_CENTER[1])
        canvas.draw_image(card_images, card_loc, CARD_SIZE, [pos[0] + CARD_CENTER[0], pos[1] + CARD_CENTER[1]], CARD_SIZE)
        
# define hand class
class Hand:
    def __init__(self):
        self.hand = []

    def __str__(self):
        str_card = ""
        for card in self.hand:
            str_card += str(card) + " "
        return "Hand Is " + str_card

    def add_card(self, card):
        self.hand.append(card)

    def get_value(self):
        # count aces as 1, if the hand has an ace, then add 10 to hand value if it doesn't bust
        value = 0
        number_ace = 0
        for card in self.hand:
            value += VALUES[card.get_rank()]
            if card.get_rank() == 'A':
                number_ace += 1
        if (number_ace != 0) and (value < 12):
            value += 10
        return value
    def draw(self, canvas, pos):
       for card in self.hand:
            pos[0] = pos[0] + CARD_SIZE[0]
            card.draw(canvas, pos)

           
# define deck class 
class Deck:
    def __init__(self):
        self.deck = []
        for suit in SUITS:
            for rank in RANKS: 
                card = Card(suit, rank)
                self.deck.append(card)
                
    def shuffle(self):
        random.shuffle(self.deck)

    def deal_card(self):
        return self.deck.pop()
    
    def __str__(self):
        str_deck = ""
        for card in self.deck:
            str_deck += str(card) + " "
        return "Deck is " + str_deck   

#define event handlers for buttons
def deal():
    global outcome, in_play, deck, dealer_hand, player_hand, loss
    deck = Deck()
    deck.shuffle()
    dealer_hand = Hand()
    player_hand = Hand()
    player_hand.add_card(deck.deal_card())
    dealer_hand.add_card(deck.deal_card())
    player_hand.add_card(deck.deal_card())
    dealer_hand.add_card(deck.deal_card())
    #print statement for testing purposes
    #print "Dealer " + str(dealer_hand),"Player " + str(player_hand)
    if in_play == True:
        loss += 1
    in_play = True

def hit():
    global in_play, deck, dealer_hand, player_hand, loss, outcome
    if in_play == True:
        # if the hand is in play, hit the player
        if (in_play == True) and player_hand.get_value() <= 21:
            player_hand.add_card(deck.deal_card())
            #print player_hand # for testing purposes
   
        # if busted, assign a message to outcome, update in_play and score
        if player_hand.get_value() > 21:
            outcome = "Player has busted, Dealer Wins!"
            loss += 1
            in_play = False
       
def stand():
    global in_play, deck, dealer_hand, player_hand, wins, loss, outcome
    if in_play == True:
        # player busts
        if player_hand.get_value() > 21:
            loss += 1
            outcome = "Player has busted, Dealer Wins!"
            in_play = False
        # if hand is in play, repeatedly hit dealer until his hand has value 17 or more
        while (in_play == True) and dealer_hand.get_value() <=16:
            dealer_hand.add_card(deck.deal_card())
            #print dealer_hand #for testing purposes
        #dealer busts    
        if dealer_hand.get_value() > 21:
            wins += 1
            outcome = "Dealer has busted, Player Wins!"
            in_play = False
        # dealer beats player    
        elif dealer_hand.get_value() >= player_hand.get_value():
            loss += 1
            outcome = "Dealer wins!"
            in_play = False

        # player beats dealer    
        elif player_hand.get_value() > dealer_hand.get_value():
            wins += 1
            outcome = "Player wins!"
            in_play = False
    

# draw handler    
def draw(canvas):
    global CANVAS_WIDTH, CANVAS_HEIGHT, CW_HALF, CH_HALF, wins, loss, outcome, in_play
    if in_play == True:
        canvas.draw_text('Hit or Stand?', (CW_HALF - (214 / 2), CH_HALF), 40, 'Black')
        dealer_hand.draw(canvas, [CW_HALF - CARD_SIZE[0] * 3, CH_HALF - CARD_SIZE[1] * 2])
        canvas.draw_image(card_back, (CARD_CENTER[0], CARD_CENTER[1]) , CARD_SIZE, [CW_HALF - CARD_CENTER[0] *3, CH_HALF - CARD_CENTER[1] * 3], CARD_SIZE)
        
    elif in_play == False:
        canvas.draw_text('Deal?', (CW_HALF - (94 / 2), CH_HALF), 40, 'Black')
        canvas.draw_text(outcome, (CW_HALF - 150, 100), 20, 'Black')
        dealer_hand.draw(canvas, [CW_HALF - CARD_SIZE[0] * 3, CH_HALF - CARD_SIZE[1] * 2])
    
    player_hand.draw(canvas, [CW_HALF - CARD_SIZE[0] * 3, CH_HALF + CARD_SIZE[1]])
    canvas.draw_text('Blackjack', (CW_HALF - (160 / 2), 30), 40, 'Black')
    canvas.draw_text('Player Record is ' + str(wins) + '-' + str(loss),\
                     (CW_HALF - (164 / 2), CH_HALF + 250), 20, 'Black')

    

# initialization frame
frame = simplegui.create_frame("Blackjack", 600, 600)
frame.set_canvas_background("Green")
#checking the text width for score, title, etc, for centering purposes
#print frame.get_canvas_textwidth("Blackjack", 40)
#print frame.get_canvas_textwidth('Player Record is ' + str(wins) + '-' + str(loss), 20)
#print frame.get_canvas_textwidth("Hit or Stand?", 40)
#print frame.get_canvas_textwidth("Deal?", 40)
#print frame.get_canvas_textwidth("Player has busted, Dealer Wins!", 40)


#create buttons and canvas callback
frame.add_button("Deal", deal, 200)
frame.add_button("Hit",  hit, 200)
frame.add_button("Stand", stand, 200)
frame.set_draw_handler(draw)


# get things rolling
deal()
frame.start()


# remember to review the gradic rubric