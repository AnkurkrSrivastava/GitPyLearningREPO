import random

print("Welcome to Rock, Paper, Scissors!")
print("Type:- 1.Rock, 2. Paper, 3. Scissors")

choices = {1: "Rock", 2: "Paper", 3: "Scissors"}
user_score = 0
computer_score = 0

for i in range(1,4):
    print(f"Round {i}:")
    # Generate computer choice
    computer = random.choice([1, 2, 3])
    # Get user input
    you = int(input("Enter your choice(1/2/3): "))
    # Validate user input
    if you not in [1, 2, 3]:
        print("Invalid choice! Please choose 1, 2, or 3.")
        continue
    # mapping the numbers to the choices
    print("You chose:", choices[you])
    print("Computer chose:", choices[computer])
    # determine the winner
    if you == computer:
        print("It's a tie!")
    else:
        if (you == 1 and computer == 3) or (you == 2 and computer == 1) or (you == 3 and computer == 2):
            print("You win!")
            user_score += 1
        else:
            print("You lose!")
            computer_score += 1
    print(f"Score: You {user_score} - Computer {computer_score}")

if user_score > computer_score:
    print("Congratulations! You are the overall winner!")
elif user_score < computer_score:
    print("Sorry! The computer is the overall winner!")
else:
    print("It's a draw overall!")   
print("Game Over!")