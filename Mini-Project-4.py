# Implementation of classic arcade game Pong

import simplegui
import random

# initialize globals - pos and vel encode vertical info for paddles
#Canvas Width
WIDTH = 600
#Canvas Height
HEIGHT = 400       
BALL_RADIUS = 20
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2
LEFT = False
RIGHT = True
#center of ball position
ball_pos = [WIDTH / 2, HEIGHT /2]
#ball velocity
ball_vel = [0, 0]
score1 = 0
score2 = 0
#center for paddle1 start
paddle1_pos = [HALF_PAD_WIDTH, 200]
paddle1_vel = [0, 0]
#center for paddle2 start
paddle2_pos = [600 - HALF_PAD_WIDTH, 200]
paddle2_vel = [0, 0]

# initialize ball_pos and ball_vel for new bal in middle of table
# if direction is RIGHT, the ball's velocity is upper right, else upper left
def spawn_ball(direction):
    global ball_pos, ball_vel # these are vectors stored as lists
    ball_pos = [WIDTH / 2, HEIGHT / 2]
    if direction == RIGHT:
        ball_vel = [-random.randrange(2, 4), \
                    -random.randrange(1, 3)]
        return ball_vel
    elif direction == LEFT:
        ball_vel = [random.randrange(2, 4),\
                    -random.randrange(1, 3)]
        return ball_vel

# define event handlers
def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel# these are numbers
    global score1, score2  # these are ints
    direction = random.choice([LEFT, RIGHT])
    spawn_ball(direction)
    score1 = 0
    score2 = 0

def draw(canvas):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel    
    # draw mid line and gutters
    canvas.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    canvas.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    canvas.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT],\
                     1, "White")
        
    # update ball
    ball_pos[0] += ball_vel[0]
    ball_pos[1] += ball_vel[1]
    #left side collision
    if ball_pos[0] <= BALL_RADIUS:
        ball_vel[0] = -ball_vel[0]
    #right side collision
    if ball_pos[0] > WIDTH - BALL_RADIUS:
        ball_vel[0] = -ball_vel[0]
    #Top collision
    if ball_pos[1] <= BALL_RADIUS:
        ball_vel[1] = -ball_vel[1]
    #bottom collision
    if ball_pos[1] > HEIGHT - BALL_RADIUS:
        ball_vel[1] = -ball_vel[1]
    #hits left gutter or paddle1
    if ball_pos[0] <= PAD_WIDTH + BALL_RADIUS:
        if paddle1_pos[1] + HALF_PAD_HEIGHT > ball_pos[1] and \
        paddle1_pos[1] - HALF_PAD_HEIGHT <= ball_pos[1]:
            ball_vel[1] = ball_vel[1] + (.1 * ball_vel[1])
            ball_vel[0] = -ball_vel[0] - (.1 * ball_vel[0])
        else:
            score2 += 1
            spawn_ball(LEFT)
    #hits right gutter or paddle2    
    if ball_pos[0] > (WIDTH - PAD_WIDTH)- BALL_RADIUS:
        if paddle2_pos[1] + HALF_PAD_HEIGHT >= ball_pos[1] and \
        paddle2_pos[1] - HALF_PAD_HEIGHT <= ball_pos[1]:
            ball_vel[1] = ball_vel[1] + (.1 * ball_vel[1])
            ball_vel[0] = -ball_vel[0] - (.1 * ball_vel[0])
        else:
            score1 += 1
            spawn_ball(RIGHT)
        
    # draw ball
    canvas.draw_circle(ball_pos, BALL_RADIUS, 20, 'White', 'White')
    # update paddle's vertical position, keep paddle on the screen
    paddle1_pos[1] += paddle1_vel[1]
    paddle2_pos[1] += paddle2_vel[1]
    #upper limit for paddle1
    if paddle1_pos[1] <= 0 + HALF_PAD_HEIGHT: 
        paddle1_vel[1] = 0
    #lower limit for paddle1
    elif paddle1_pos[1] > 400 - HALF_PAD_HEIGHT:
        paddle1_vel[1] = 0
    #upper limit for paddle2
    if paddle2_pos[1] <= 0 + HALF_PAD_HEIGHT: 
        paddle2_vel[1] = 0
    #lower limit for paddle2
    elif paddle2_pos[1] > 400 - HALF_PAD_HEIGHT:
        paddle2_vel[1] = 0
    
    # draw paddles
    canvas.draw_line((paddle1_pos[0], paddle1_pos[1] + HALF_PAD_HEIGHT), \
                     (paddle1_pos[0], paddle1_pos[1] - HALF_PAD_HEIGHT) ,\
                     PAD_WIDTH, 'White')
    canvas.draw_line((paddle2_pos[0], paddle2_pos[1] + HALF_PAD_HEIGHT), \
                      (paddle2_pos[0], paddle2_pos[1] - HALF_PAD_HEIGHT),\
                      PAD_WIDTH, 'White')
    # draw scores
    canvas.draw_text(str(score1), (100, 50), 30, 'White')
    canvas.draw_text(str(score2), (500, 50), 30, 'White')
        
def keydown(key):
    #left paddle control
    global paddle1_vel, paddle2_vel
    if key == simplegui.KEY_MAP['w']:
        paddle1_vel[1] = -4
    elif key == simplegui.KEY_MAP['s']:
        paddle1_vel[1] = 4
    #right paddle control
    if key == simplegui.KEY_MAP['up']:
        paddle2_vel[1] = -4
    elif key == simplegui.KEY_MAP['down']:
        paddle2_vel[1] = 4
    
   
def keyup(key):
    global paddle1_vel, paddle2_vel
    #left paddle control
    global paddle1_vel, paddle2_vel
    if key == simplegui.KEY_MAP['w']:
        paddle1_vel[1] = 0
    elif key == simplegui.KEY_MAP['s']:
        paddle1_vel[1] = 0
    #right paddle control
    if key == simplegui.KEY_MAP['up']:
        paddle2_vel[1] = 0
    elif key == simplegui.KEY_MAP['down']:
        paddle2_vel[1] = 0
    
# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
button1 = frame.add_button('Reset', new_game)


# start frame
new_game()
frame.start()
