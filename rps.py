'''
------------------------------------------------
Title: Simple Variable-Size Rock, Paper, Scissors.
Author: Alexander Cantrell
------------------------------------------------

Basic RPS (rock, paper, scissors) is played by default. To play RPSLS (rock, paper,
scissors, lizard, spock) comment the current name_mappings, and uncomment the
game-specific one. You can also add your own options as long as the follow the input
rules below.

Input Rules:
This game, much like normal RPS, or its extension RPSLS, relies on the number of
options being odd in order for balance to be maintained. If this were not the case,
diferent options would have lower or higher chances of winning. The proof of this is
left up to the reader as an exercise.
Aside from this requirement of odd-ness, there are no specific game-related input rules,
however there are some semantic ones. Specifically, the key for each option must be
unique or the game will break. Lastly, the options must be input in order of their increasing
cyclical dominance. This will allow the code to dynamically determine all other dominances
and preserve cyclical dominance while running.

Dominance Mapping:
Dominance is decided based on the rules of RPS and its extension RPSLS. In these games,
each option has an equivalent number of options it dominates, and is dominated by (rock beats
scissors & paper beats rock) which, when summed, are equal to the total number of other options
available. For basic gameplay (RPS) there is only one unique solution for cyclical dominance which
is enough to maintain this requirement, but for higher dimensional gameplay (RPSLS), there exist
several unique solutions for cyclical dominance which are required for our rules to be satisfied.
Thus, we borrow the further dominance rules from the RPSLS model by maintaining that every option
dominates the option that dominates its dominator. More specifically, taking the subset of any
three options as nodes, we create a directed cyclic graph where edge direction denotes domination.
More simply, we create a game of RPS with each set of three options. In this way we are able to
fully generate our dominance map for any set of options.

'''

import random

name_mappings = {'r':'Rock','p':'Paper','s':'Scissors'}
#Uncomment for Rock Paper Scissors Lizard Spock
#name_mappings = {'r':'Rock','p':'Paper','sc':'Scissors','sp':'Spock','l':'Lizard'}

#Get list of allowed options
options = list(name_mappings.keys()) 

#Generate "let's play" and "options" strings dynamically for changing game types
option_string = ''
name_string = ''
for key, value in name_mappings.items():
    option_string += f'{value}({key}), '
    name_string += f'{value}, '

#Generate value mappings. (Iterate over list assigning each option to an integer [0,N)
value_mappings = {options[index]: index for index in range(len(options))}

print(f"Let's Play {name_string}") #Announce game start

#Game Loop
while True:
    #Get cpu choice and the value mapping
    cpu_choice = random.choice(options)
    cpu_value = value_mappings[cpu_choice]

    #Get user choice and value mapping
    user_choice = None
    while user_choice not in options: #Loop until user input is valid
        user_choice = input(f"Make Your Choice: , {option_string}? ")
        if user_choice not in options: #Validation condition
            print("Invalid Option, Please Try Again...")
    user_value = value_mappings[user_choice]

    '''
    By mapping the options to integer values, we can perform some interesting math.
    Subtracting the cpu choice value from the user choice value, we get one of five options:
    0 -> Tie
    Even Positive -> User Loss
    Even Negative -> User Win
    Odd Positive -> User Loss
    Odd Negative -> User Win
    The proof of this is left to the reader as an exercise :)

    After this subtraction, we simplify our outcome by adding one if the outcome is above 0.
    This is accomplished by adding the boolean value (outcome>0) as True == 1 and False == 0
    for basic boolean values in Python. This gives us three options:
    0 -> Tie
    Even -> User Win
    Odd -> User Loss

    Thus, after checking if the outcome is 0, all that is needed is to check if the outcome
    is even or odd via the modulus 2.
    '''
    outcome = (user_value-cpu_value)
    outcome = outcome + (outcome > 0)

    if outcome == 0: #Check for ties
        print(f"Tie! You Both Chose {name_mappings[cpu_choice]}!")
    elif outcome % 2 : #If odd -> 1 == True, if even -> 0 == False
        print(f"You Lose! {name_mappings[cpu_choice]} Beats {name_mappings[user_choice]}!")
    else:
        print(f"You Win! {name_mappings[user_choice]} Beats {name_mappings[cpu_choice]}!")
        

    #Ask to play again
    if input("Play Again? (y/n): ") == 'n':
        break
