# 5 rounds tournament 
# random choice for the computer
# the first player win 3 times wins the game

import random
import os

def clean_trminal():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def rules_brief(name):
    print(f"""
        # Welcome {name} to the Rock Paper Scissors Tournament!
        # The rules are simple:
        # - For Rock, press [R]
        # - For Paper, press [P]
        # - For Scissors, press [S]

        # There are 5 rounds.
        # The player who wins 3 rounds first is the tournament winner.

        # Let's begin!
          """)
    

def computer_play():
    options = ["r", "s", "p"]
    computer_choice = random.choice(options)
    return computer_choice


def who_win_the_round(player,computer):
    rules= {
        "r":"s",
        "p":"r",
        "s":"p",
    }
    if rules[player] == computer:
        return "player"
    elif rules[computer] == player:
        return "computer"
    else:
        return False
    


rounds=0
player_score=0
computer_score=0
user_name = input("Enter your name: ")
rules_brief(user_name)

while True:
    player_choice = input("Enter your choice: ").lower()
    if player_choice not in ["r", "s", "p"]:
        print("Invalid option! Only [R], [S], or [P] are allowed.")
    else:  
        computer_choice= computer_play()
        rounds += 1
        win = who_win_the_round(player_choice,computer_choice)
        if win == "player":
            player_score += 1
            print(f"{user_name} wins the round!")
        elif win == "computer":
            computer_score += 1
            print("Computer wins the round!")
        elif win == False:
            print("It's even!")
    if player_score == 3:
        print(f"{user_name} wins the tournament!")
        break    
    elif computer_score == 3:
        print("Computer wins the tournament!")
        break
    elif rounds == 5:
        user_continue = input("The tournament ends in even. You can try to beat the computer again by pressing [A]. To quit, press [Q]: ").lower()
        if user_continue == 'a':
            rounds=0
            player_score=0
            computer_score=0 
            clean_trminal()   
        elif user_continue == 'q':
            clean_trminal() 
            print("Goodbye!")
            break
        else:
            print("Invalid option! Only [A] or [Q] are allowed.")
        
    
    




    
  
    

    
    

