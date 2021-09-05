import random

#Input the stop number in range
top_of_range = input("Type a number: ")      

if top_of_range.isdigit():                                                             
    top_of_range = int(top_of_range)
    if top_of_range <= 0:
        print("Please type a number larger than 0 next time.")
        quit()
else:
    print("Please type a number.")
    quit()

#Randomize the guessing number & set the number of guess
random_number = random.randint(0, top_of_range)
times_of_guess = 0

#Have user input their guessing number
while True:
    times_of_guess += 1
    user_guess = input("Make your guess between 0 and your input number: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print("Please type a number.")
        continue
#Make the rules and condition for the guessing
    if user_guess == random_number:
        print("You got it!")
        break
    elif user_guess > random_number:
        print("Your guess is above the number.")
    else:
        print("Your guess is below the number.")

print("You got it in", times_of_guess, "guesses")