# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console

import simplegui
import random
import math

#Global Variables
#num_range is the range for that game
#tries_left is the number of guesses remaining in the game
#secret_number is number we are trying to guess
num_range = 100

# helper function to start and restart the game
def new_game():
    # Generating the random secret number based on num_range
    global secret_number
    secret_number = random.randrange(0, num_range)
    #setting the number of guesses based on the number range
    #of the game
    global tries_left
    if num_range == 100:
        tries_left = 7
    else: 
        tries_left = 10
    #Printing statements for guesses left and range
    #at the start of the game
    print "Number of Guesses is " + str(tries_left)
    print "New Game. Range is 0-" + str(num_range)

# Event Handler for game with range of 100
def range100():
    # button that changes the range to [0,100) and starts a new game 
    global num_range
    num_range = 100
    global secret_number
    secret_number = random.randrange(0, num_range)
    print ""
    new_game()

#Event Handler for game with range of 1000
def range1000():
    # button that changes the range to [0,1000) and starts a new game
    global num_range
    num_range = 1000
    global secret_number
    secret_number = random.randrange(0, num_range)
    print ""
    new_game()

#Event Handler for Game Logic    
def input_guess(guess):
    # convert guess from string to integer	
    player_guess = int(guess)
    # decrement counter for guesses
    global tries_left
    tries_left -= 1
    #printing blank line and  what player's guess was
    print ""
    print "Guess was " + str(player_guess)
    # Tells player they are out of guesses and displays secret number
    if tries_left == 0 and player_guess is not secret_number:
        print "Out of Guesses. Secret Number is " + str(secret_number)
        print "Starting New Game"
        print ""
        new_game()
    # Player Guessed Correctly on Last Try
    elif tries_left == 0 and player_guess == secret_number:
        print "Correct on Last Try!"
        print "Starting New Game"
        print ""
        new_game()
     # Player needs to guess a lower number and prints remaining guesses
    elif player_guess > secret_number and tries_left > 0:
        print "Number of guesses remaining is " + str(tries_left)
        print"Lower!"
    # Player needs to guess a higher number and prints remaining guesses
    elif player_guess < secret_number and tries_left > 0:
        print "Number of guesses remaining is " + str(tries_left)
        print "Higher!"
    #Player has won
    elif player_guess == secret_number:
        print "Correct! Well Played!"
        print "Starting New Game"
        print ""
        new_game()
    #Error Message, Restart Game
    else: 
        print "Error. Starting New Game"
        print ""
        new_game()
    
# create window
frame = simplegui.create_frame("Guess the Number", 250, 250)

# register event handlers for control elements and start frame
frame.add_button("Range is [0, 100)", range100, 200)
frame.add_button("Range is [0, 1000)", range1000, 200)
frame.add_input("Enter a guess", input_guess, 200)
frame.start()

# call new_game 
new_game()

# always remember to check your completed program against the grading rubri