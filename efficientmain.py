import random

def get_computer_choice():
    #"""Randomly select a choice for the computer."""
    choices = ["rock", "paper", "scissors"]
    return random.choice(choices)

def get_player_choice():
    #"""Get the player's choice."""
    choice = input("Enter your choice (rock, paper, or scissors): ").lower()
    while choice not in ["rock", "paper", "scissors"]:
        print("Invalid choice. Please choose 'rock', 'paper', or 'scissors'.")
        choice = input("Enter your choice (rock, paper, or scissors): ").lower()
    return choice

def determine_winner(player_choice, computer_choice):
    #"""Determine the winner of the game."""
    if player_choice == computer_choice:
        return "It's a tie!"
    elif (player_choice == "rock" and computer_choice == "scissors") or \
         (player_choice == "paper" and computer_choice == "rock") or \
         (player_choice == "scissors" and computer_choice == "paper"):
        return "You win!"
    else:
        return "Computer wins!"

def play_game():
   # """Play a game of Rock, Paper, Scissors."""
    print("Welcome to Rock, Paper, Scissors!")
    player_choice = get_player_choice()
    computer_choice = get_computer_choice()
    print(f"Computer chose: {computer_choice}")
    result = determine_winner(player_choice, computer_choice)
    print(result)

#The if __name__ == "__main__": block allows you to specify code that should 
#only run when the script is executed directly, and not when it is imported as a module.
if __name__ == "__main__":
    play_game() 
