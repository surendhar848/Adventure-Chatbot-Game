import random

def get_computer_choice():
    """Randomly selects a choice for the computer."""
    choices = ["rock", "paper", "scissors"]
    return random.choice(choices)

def get_winner(user_choice, computer_choice):
    """Determines the winner based on user and computer choices."""
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "paper" and computer_choice == "rock") or \
         (user_choice == "scissors" and computer_choice == "paper"):
        return "You win!"
    else:
        return "You lose!"

def is_valid_choice(choice):
    """Checks if the user input is valid."""
    return choice in ["rock", "paper", "scissors"]

def play_game():
    """Main function to play the game."""
    print("Welcome to Rock, Paper, Scissors!")
    
    while True:
        # User input with validation
        user_choice = input("Enter rock, paper, or scissors: ").lower()
        
        if not is_valid_choice(user_choice):
            print("Invalid choice! Please enter rock, paper, or scissors.")
            continue
        
        computer_choice = get_computer_choice()
        print(f"Computer chose: {computer_choice}")
        
        # Get result
        result = get_winner(user_choice, computer_choice)
        print(result)
        
        # Ask if user wants to play another round
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            print("Thanks for playing!")
            break

if __name__ == "__main__":
    play_game()
