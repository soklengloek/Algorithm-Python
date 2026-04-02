import random

def guess_number_game():
    """A simple number guessing game."""
    number = random.randint(1, 10)
    attempts = 0 
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 10.")  
    while True:
        try:
            guess = int(input("Take a guess: "))
            attempts += 1
            
            if guess < number:
                print("Too low! Try again.")
            elif guess > number:
                print("Too high! Try again.")
            else:
                print(f"You got it! The number was {number}.")
                print(f"It took you {attempts} attempts.")
                break
        except ValueError:
            print("Please enter a valid number.")
if __name__ == "__main__":
    guess_number_game()