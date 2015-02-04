# Rock-paper-scissors-lizard-Spock template


# The key idea of this program is to equate the strings
# "rock", "paper", "scissors", "lizard", "Spock" to numbers
# as follows:
#
# 0 - rock
# 1 - Spock
# 2 - paper
# 3 - lizard
# 4 - scissors

# helper functions

#Function to convert names to number
def name_to_number(name):
    if "rock" == name:
        return 0
    elif "Spock" == name:
        return 1
    elif "paper" == name:
        return 2
    elif "lizard" == name:
        return 3
    elif "scissors" == name:
        return 4
    else:
        return "Not a valid play" 

#Function to convert numbers to names
def number_to_name(number):
    if 0 == number:
        return "rock"
    elif 1 == number:
        return "Spock"
    elif 2 == number: 
        return "paper"
    elif 3 == number:
        return "lizard"
    elif 4 == number:
        return "scissors"
    else:
        return "Not a valid play"

def rpsls(player_choice):
    print ""
    print "Player chooses " + player_choice
    player_number = name_to_number(player_choice)
    import random
    comp_number = random.randrange(0, 4) 
    comp_choice = number_to_name(comp_number)
    print "Computer chooses " + comp_choice
    diff = (player_number - comp_number) % 5
    if diff > 2:
        print "Computer Wins!"
    elif diff <= 2 and diff > 0:
        print "Player Wins!"
    else:
        print "Player and Computer Tie!"
    

rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")

# always remember to check your completed program against the grading rubric


