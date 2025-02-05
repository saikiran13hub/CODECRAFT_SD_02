import random

def guess_the_number():
    print("Welcome to the Number Guessing Game!")
    number_to_guess = random.randint(1, 100)
    attempts = 0

    while True:
        try:
            user_guess = int(input("Enter your guess (between 1 and 100): "))
            attempts += 1

            if user_guess < 1 or user_guess > 100:
                print("Please enter a number between 1 and 100.")
                continue

            if user_guess < number_to_guess:
                print("Too low! Try again.")
            elif user_guess > number_to_guess:
                print("Too high! Try again.")
            else:
                print(f"Congratulations! You guessed the number {number_to_guess} in {attempts} attempts.")
                break
        except ValueError:
            print("Invalid input. Please enter a valid number.")
guess_the_number()
