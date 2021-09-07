import random

user_score = 0
computer_score = 0

options = ["rock", "paper", "scissors"]

while True:
    user_input = input("Hi there, Rock/Paper/Scissors or Quit (Press Q)?\n").lower()
    if user_input == "q":
        break
    if user_input not in options: #if user types a wrong pick, the program will ask for their choice again
        continue

    random_number = random.randint(0,2)
    #rock: 0, paper: 1, scissors: 2
    computer_pick = options[random_number]
    print("Computer picks", computer_pick + ".")

    #user wins
    if user_input == "rock" and computer_pick == "scissors":
        user_score += 1
        print("You got one point!\n")
    elif user_input == "paper" and computer_pick == "rock":
        user_score += 1
        print("You got one point!\n")
    elif user_input == "scissors" and computer_pick == "paper":
        user_score += 1
        print("You got one point!\n")
    
    elif user_input == computer_pick: #Both picks the same
        print("Draw\n")

    else: #Computer wins
        computer_score += 1
        print("Computer got one point!\n")


print("You:", user_score, "Computer:", computer_score)

#Final result
if user_score > computer_score:
    print("Congratulations! You win!")
elif user_score == computer_score:
    print("Deuce")
else: 
    print("Lew lew! Computer wins!")

print("Bye-bye!\n")
