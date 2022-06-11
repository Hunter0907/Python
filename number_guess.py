
import random
# importing the python package random


random_num = random.randint(1, 9)
# Generate a random number between 1 and 10

guess_limit = 5
# Set the limit of guesses to 5
guess_count = 1
# Set the guess count to 1

print("Welcome to the number guessing game!\nYou have 5 tries to guess the number between 1 and 9.\nGood luck!")
# Print the welcome message

while guess_limit > 0:
    # While the guess limit is greater than 0

    guess = int(input("Guess a number: "))
    # Get the user input for the guess

    if guess == random_num:
        print("You guessed it!")
        # Printing the string "You guessed it!"
                
        print("\nCorrect!!!\nIt took you", guess_count, "guess(es).\n")
        # Printing the string "Correct!!!\nIt took you X guess(es).\n"
        
        break
        # Breaking out of the loop
        
    if guess > random_num:
        # If the guess is not equal to the random number
        
        print("Number Guess is Too high!")
        # Printing the string "Your guess is too high!"
        
        guess_limit -= 1
        # Decrementing the guess limit
        guess_count += 1
        # Incrementing the guess count
        
        print(guess_limit, "guesses left.\n")
        # Printing the string "X guesses left.\n"

    if guess < random_num:
        # If the guess is not equal to the random number
        
        print("Number Guess is Too low!")
        # Printing the string "Your guess is too low!"
        
        guess_limit -= 1
        # Decrementing the guess limit
        guess_count += 1
        # Incrementing the guess count
        
        print(guess_limit, "guesses left.\n")
        # Printing the string "X guesses left.\n"

    if guess_limit == 0:
        # If the guess limit is 0
        print("You ran out of guesses.\nThe number was", random_num, ".")
        # Printing the string "You ran out of guesses.\nThe number was X."