import random

def play_game():
    choices = ['rock', 'paper', 'scissors']
    computer_choice = random.choice(choices)
    user_choice = input("Enter your choice (rock, paper, or scissors): ").lower()

    while user_choice not in choices:
        print("Invalid choice. Please try again.")
        user_choice = input("Enter your choice (rock, paper, or scissors): ").lower()

    print(f"Computer chose: {computer_choice}")
    print(f"You chose: {user_choice}")

    if user_choice == computer_choice:
        print("It's a tie!")
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'paper' and computer_choice == 'rock') or \
         (user_choice == 'scissors' and computer_choice == 'paper'):
        print("You win!")
        play_game.user_score += 1
    else:
        print("Computer wins!")
        play_game.computer_score += 1

    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again == 'yes':
        play_game()
    else:
        print(f"Final Scores: User - {play_game.user_score}, Computer - {play_game.computer_score}")

play_game.user_score = 0
play_game.computer_score = 0
play_game()


