# template for "Stopwatch: The Game"
import simplegui
# define global variables
ticks = 0
guess_correct = 0
total_guess = 0

# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(ticks):
    a = ticks / (10 * 60) % 10
    b = (ticks / 10 % 60) / 10
    c = ticks / 10 % 10
    d = ticks % 10
    return str(a)+':'+str(b)+str(c)+'.'+str(d)  
    
# define event handler for start button
def button_start():
    timer.start()
# event handler for stop button
def button_stop():
    global ticks
    if timer.is_running():
        timer.stop()
        if (ticks % 10) == 0:
            global guess_correct
            guess_correct += 1
            global total_guess
            total_guess += 1
        else:
            total_guess += 1

#defining handler for reset button     
def button_reset():
    timer.stop()
    global ticks
    global guess_correct
    global total_guess
    ticks = 0
    guess_correct = 0
    total_guess = 0
    
# define event handler for timer with 0.1 sec interval
def time_handler():
    global ticks
    ticks += 1

timer = simplegui.create_timer(100, time_handler)
timer.start()

# define draw handler
def draw_handler(canvas):
    canvas.draw_text(format(ticks), (75, 110), 30, 'Red')
    canvas.draw_text(str(guess_correct)+'/'+str(total_guess), (165, 30), 20, 'Red')
    
    
# create frame
frame = simplegui.create_frame("Stopwatch", 200, 200)


# register event handlers
frame.set_draw_handler(draw_handler)
button1 = frame.add_button('Start', button_start, 100)
button2 = frame.add_button('Stop', button_stop, 100)
button3 = frame.add_button('Reset', button_reset, 100)
# start frame
frame.start()

# Please remember to review the grading rubric
