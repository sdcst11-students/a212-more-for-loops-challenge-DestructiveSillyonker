#!python3

'''
Create a number guessing game
There is a limit of 10 guesses
The program will ask the user to enter an integer from 1 to 100
The program will then tell the user if the number is too high, too low or correct.
If the number is correct, the program will end
If the 10 guesses are used up, the program will say that the user has lost
'''
import random
Number = random.randint(1,100)


input("------------------------Lets play a game------------------------\n---------------------Press enter to continue--------------------")
print("     ")
print("     ")
print("     ")
print("     ")
print("     ")
print("     ")
print("     ")
for i in range(1,11):
    Guess = int(input("Geuss a number from 1-100: "))

    if Guess > Number:
        print(f"{Guess} is Cold, Try lower")

    if Guess < Number:
        print(f"{Guess} is Cold, Try higher")

    if Guess == Number:
        print(f"{Guess} is Correct!")
        break
else:
    print(f"{Number} was the number, come on that was easy!")