import random

print("Welcome to Rock, Paper, Scissors!")
print("Type:- 1.Rock, 2. Paper, 3. Scissors")

# Generate computer choice
computer = random.choice([1, 2, 3])

# Get user input
you = int(input("Enter your choice(1/2/3): "))

# Validate user input
if you not in [1, 2, 3]:
    print("Invalid choice! Please choose 1, 2, or 3.")
else:
#mapping the numbers to the choices
    choices = {1: "Rock", 2: "Paper", 3: "Scissors"}

    print("You chose:", choices[you])
    print("Computer chose:", choices[computer])
#determine the winner
    if you == computer:
        print("It's a tie!")
    else:
        if (you == 1 and computer == 3) or (you == 2 and computer == 1) or (you == 3 and computer == 2):
            print("You win!")
        else:
            print("You lose!")


