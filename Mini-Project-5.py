# implementation of card game - Memory
import simplegui
import random
#globals
#card 1 when selecting it during game
card_1 = [0, 0]
#card 2 when seleciting in during game
card_2 = [0, 0]
#state for memory
state = 0
#for counting number of turns
turns = 0
# helper function to initialize globals
def new_game():
    #2 smaller lists to combine into card deck
    global deck
    deck = range(8)
    deck.extend(range(8))
    random.shuffle(deck)
    #print deck  #for testing
    global state
    state = 0
    global exposed
    exposed = [False] * 16
    global turns
    turns = 0
    label.set_text("Turns = 0")
 
# define event handlers
def mouseclick(pos):
    global exposed, deck, state, turns, card_1, card_2
    #index position of click
    i = pos[0] // (800 // len(deck))
    if exposed[i] == False:
        if state == 0:
            state = 1
            card_1 = [deck[i], i]
        elif state == 1: 
            state = 2
            card_2 = [deck[i], i]
            turns += 1
            label.set_text('Turns = ' +str(turns))
        else: 
            state = 1
            if card_1[0] != card_2[0]:
                exposed[card_1[1]] = False
                exposed[card_2[1]] = False
            card_1[0] = deck[i]
            card_1[1] = i
    exposed[i] = True

# cards are logically 50x100 pixels in size    
def draw(canvas):
    #card position (c_pos) and text position (t_pos)
    c_pos = [0, 0]
    t_pos = [20, 60]
    for i in range(16):
        card = deck[i]
        if exposed[i] == True:
            canvas.draw_text(str(card), t_pos, 30, 'White')
        else:
             canvas.draw_polygon([[c_pos[0], c_pos[1]], [c_pos[0], c_pos[1] + 100],\
                                [c_pos[0] + 50,c_pos[1] + 100],[c_pos[0] + 50, c_pos[1]]],\
                                1, "White", "Green")    
        c_pos[0] += 50
        t_pos[0] += 50

# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Reset", new_game)
label = frame.add_label('Turns = ')


# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
new_game()
frame.start()


# Always remember to review the grading rubric