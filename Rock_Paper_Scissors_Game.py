"""
Rock Paper Scissors is a hand game usually played between two people. In this 
game, scissors can beat paper, paper can beat rock, and rock can beat scissors


To create and play rock paper scissors, I will be using the if and elif statements in 
Python. I will prepare this game to be played between two players. Player-1 will be 
the user, and player-2 will be the computer. Player one will manually select the rock 
paper or scissor, while player two will choose randomly. So I will also use the 
random module in Python to create this game.
"""


# import random

# player1 = input("Select Rock, Paper, or Scissor :").lower()
# player2 = random.choice(["Rock", "Paper", "Scissor"]).lower()
# print("Player 2 selected: ", player2)

# if player1 == "rock" and player2 == "paper":
#     print("Player 2 Won")
# elif player1 == "paper" and player2 == "scissor":
#     print("Player 2 Won")
# elif player1 == "scissor" and player2 == "rock":
#     print("Player 2 Won")
# elif player1 == player2:
#     print("Tie")
# else:
#     print("Player 1 Won")import random






"""
The above code is just simply showing rock paper scissor for one attempt.
in updated code what i done is i choose two players with score 0 and make it 
3 game match the player who have most of the win, will win the match and i use 
if, elif statements here for it.
"""

import random

# Initialize scores
player1_score = 0
player2_score = 0

# Best of 3 attempts
for i in range(3):
    player1 = input("Select Rock, Paper, or Scissor: ").lower()
    player2 = random.choice(["Rock", "Paper", "Scissor"]).lower()
    print(f"Attempt {i+1}: Player 2 selected: {player2}")

    if player1 == "rock" and player2 == "paper":
        print("Player 2 Won this round")
        player2_score += 1
    elif player1 == "paper" and player2 == "scissor":
        print("Player 2 Won this round")
        player2_score += 1
    elif player1 == "scissor" and player2 == "rock":
        print("Player 2 Won this round")
        player2_score += 1
    elif player1 == player2:
        print("It's a Tie this round")
    else:
        print("Player 1 Won this round")
        player1_score += 1

# Determine the overall winner
if player1_score == 3:
    print("Fabulous! Undefeated victory for Player 1!")
elif player1_score == 2:
    print("Congratulations! Player 1 won best of 3!")
elif player2_score == 3:
    print("Fabulous! Undefeated victory for Player 2!")
elif player2_score == 2:
    print("Congratulations! Player 2 won best of 3!")
else:
    print("It's a tie overall!")






