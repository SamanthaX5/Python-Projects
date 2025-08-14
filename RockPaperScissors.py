import random


def get_computer_choice():
    """comp Random select rock/paper/scissors"""
    return random.choice(["rock", "paper", "scissors"])

def get_user_choice():
    """ask user for their choice"""
    choice = input("Enter rock, paper, or scissors: ").lower()
    while choice not in ["rock", "paper", "scissors"]:
     choice = input("Invalid choice. Please enter rock, paper, or scissors: ").lower()
    return choice


def determine_winner(user, computer):
    """Determine winner."""
    if user == computer:
        return "VICTORY DENIED TO BOTH!"
    elif (user == "rock" and computer == "scissors") or \
        (user == "paper" and computer == "rock") or \
        (user == "scissors" and computer == "paper"):
     return "YOU WIN!!"
    else:
     return "WOMP WOMP!"


def play_game():
    print("=== LETS PLAY ROCK PAPER SCISSORS! ===")
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()

    print(f"\nYou chose: {user_choice}")
    print(f"Computer chose: {computer_choice}")

    result = determine_winner(user_choice, computer_choice)
    print(result)


if __name__ == "__main__":
 play_game()