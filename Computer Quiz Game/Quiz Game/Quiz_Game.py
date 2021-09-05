print("Welcome to the quiz game!")

playing = input("Do you want to play? ")

if playing.lower() != "yes":
    quit()

print("Okay! Let's play :D")

score = 0

answer = input("What does CPU stand for? ").lower()
if answer == "central processing unit":
    print("Yay! You're correct!")
    score += 1
else: print("What a pity!")

answer = input("What does GPU stand for? ").lower()
if answer == "graphics processing unit":
    print("Yay! You're correct!")
    score += 1
else: print("What a pity!")

answer = input("What does RAM stand for? ").lower()
if answer == "random accessing memory":
    print("Yay! You're correct!")
    score += 1
else: print("What a pity!")

answer = input("What does PSU stand for? ").lower()
if answer == "power supply unit":
    print("Yay! You're correct!")
    score += 1
else: print("What a pity!")

print("You got " + str(score) + " question correct!")
print("You got " + str(score / 4 * 100) + "% question correct!")