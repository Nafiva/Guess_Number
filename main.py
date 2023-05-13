import random

def guess_the_number():
    secret_number = random.randint(1, 250)
    attempts = 0

    while True:
        attempts += 1
        guess = int(input("Guess a number between 1 and 250: "))

        if guess < secret_number:
            print("Too low, Try Again!")
        elif guess > secret_number:
            print("Too high!")
        else:
            print(f"Congratulations! You guessed the number in {attempts} attempts.")
            break

guess_the_number()