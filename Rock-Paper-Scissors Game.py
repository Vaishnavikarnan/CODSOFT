# VAISHNAVI.K_PYTHON INTERNSHIP
# rock-paper-scissors game_TASK4

import random

def get_computer_choice():
    choices = ['rock', 'paper', 'scissors']
    return random.choice(choices)

def get_user_choice():
    choice = input("Enter your choice (rock, paper, or scissors): ").lower()
    while choice not in ['rock', 'paper', 'scissors']:
        print("Invalid choice, please try again.")
        choice = input("Enter your choice (rock, paper, or scissors): ").lower()
    return choice

def decide_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "tie"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'scissors' and computer_choice == 'paper') or \
         (user_choice == 'paper' and computer_choice == 'rock'):
        return "user"
    else:
        return "computer"

def display_result(user_choice, computer_choice, winner):
    print(f"\nYou chose: {user_choice}")
    print(f"Computer chose: {computer_choice}")
    
    if winner == "tie":
        print("It's a tie!")
        print("No Points")
    elif winner == "user":
        print("You win!")
        print("You won 1 points")
    else:
        print("You lose!")

def play_again():
    choice = input("Do you want to play again? (yes or no): ").lower()
    return choice == 'yes'

def welcome_message():
    print("===================================")
    print("Greetings and welcome to the game of rock, paper, scissors")
    print("===================================")
    print("Instructions:")
    print("1. You will be playing against the computer.")
    print("2. Choose either 'rock', 'paper', or 'scissors' when prompted.")
    print("3. Rock beats scissors, scissors beat paper, and paper beats rock.")
    print("4. The game will keep track of your points.")
    print("5. Have fun and good luck!")
    print("===================================\n")

def farewell_message():
    print("Regards for participating!")

def main():
    user_points = 0
    computer_points = 0
    
    welcome_message()
    
    while True:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        winner = decide_winner(user_choice, computer_choice)
        
        display_result(user_choice, computer_choice, winner)
        
        if winner == "user":
            user_points += 1
        elif winner == "computer":
            computer_points += 1
        
        print(f"\nPoints: You - {user_points}, Computer - {computer_points}")
        
        if not play_again():
            farewell_message()
            break

if __name__ == "__main__":
    main()
