# bad aim code by seal himself, no gpt 

import time
import random

# create random integer between min and max

minimum = 1
maximum = 100

rand = random.randint(minimum,maximum)

# useless print cuz it looks nice
print("Code Start")

time.sleep(1)

print("\n")

# hint on number possibilities
if (rand < (maximum/2)):
    print("Number is less than", (maximum/2))
else:
    time.sleep(0)

if (rand > (maximum/2)):
    print("Number is greater than", (maximum/2))
else:
    time.sleep(0)
    
if (rand == (maximum/2)):
    print("Number IS", (maximum/2))
    
answer = input("Guess a number: ")
# user input guess, while loop to continue guessing
while True:

    if int(answer) > (maximum):
        print("The number you entered is too big for the constraints.")
    elif int(answer) < (minimum):
        print("The number you entered is too small for the constraints.")
    elif int(rand) == int(answer):
         print("Correct answer!")
         break
    elif int(rand) > int(answer):
        print("The number is greater than the guessed number.")
    else:
        print("The number is less than the guessed number.")
    answer = input("Guess again: ")
    

input("Enter to exit.")