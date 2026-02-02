import random
rps = ["rock", "paper", "scissors"]
while True:
    user = input("Enter rock, paper, or scissors (or 'quit' to stop): ")
    if user == "quit":
        break
    computer = random.choice(rps)
    print(f"Computer chose: {computer}")
    if user == computer:
        print("It's a tie!")
    elif (user == "rock" and computer == "scissors") or \
        (user == "paper" and computer == "rock") or \
        (user == "scissors" and computer == "paper"):
        print("You win!")
    else:
        print("Computer wins!")