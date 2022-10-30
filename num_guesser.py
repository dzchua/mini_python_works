from random import *

l = 8
r = randint(1, 5)
guess = 0
count = 1
while count < 9:
    guess = int(input("Guess a number from 1 - 5 \n"))
    # if count > 7:
    #     # print("Counter: ", count)
    #     break
    if guess < 1 or guess > 5:
        print("Out of range")
    elif guess == r:
        print("You guessed it!")
        print("The number of times you guessed: ", count)
        break
    elif guess > r:
        print("Choose smaller number")
    elif guess < r:
        print("Choose bigger number")

    count += 1
if guess != r:
    print("Correct answer: ", r)
