import random

# Define choices
choices = {"r": "Rock", "p": "Paper", "s": "Scissors"}
# Map choices to win/lose conditions
results = {
    ("Rock", "Scissors"): "You win!",
    ("Paper", "Rock"): "You win!",
    ("Scissors", "Paper"): "You win!",
    ("Scissors", "Rock"): "You lose!",
    ("Rock", "Paper"): "You lose!",
    ("Paper", "Scissors"): "You lose!",
}

# Get computer's choice
computer_choice = random.choice(list(choices.values()))

# Get user's choice
user_input = input("Enter your choice (r for Rock, p for Paper, s for Scissors): ")
user_choice = choices[user_input]

# Display choices
print(f"You chose: {user_choice}")
print(f"Computer chose: {computer_choice}")

# Determine the result
if computer_choice == user_choice:
    print("It's a draw!")
else:
    print(results.get((user_choice, computer_choice), "Something went wrong!"))
