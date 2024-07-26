import random

computer = random.choice([1, 0, -1])
you = int(input("Enter your choice (1 for rock, 0 for paper, -1 for scissors): "))
youDict = {1: "rock", -1: "paper", 0: "scissors"}

print(f"Computer chose: {youDict[computer]}")
print(f"You chose: {youDict[you]}")

if computer == you:
    print("It's a draw")
elif (computer == -1 and you == 1) or (computer == 1 and you == 0) or (computer == 0 and you == -1):
    print("You win!")
else:
    print("Computer wins!")