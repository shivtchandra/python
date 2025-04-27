import random



def guess_number():
    num = random.randint(1, 100)
    attempts = 0

    god = True

    while god:
        attempts += 1
        guess = int(input ("Guess the number: "))
        if guess < num:
            print("Too low!")
        elif guess > num:
            print("Too high!")
        else:
            print(f"Congratulations! You guessed the number {num} in {attempts} attempts.")
            god = False
        if ans == "easy":

            print(f"You have  attempts")

            if attempts > 10:
                god = False
                print("You lose!")
        elif ans == "medium":

            print(f"You have  attempts")

            if attempts > 7:
                god = False
                print("You lose!")
        elif ans == "hard":
            print(f"You have  more attempts")

            if attempts > 5:
                god = False
                print("You lose!")

        else:
            print("Invalid level. Please choose easy, medium, or hard.")
            return

print("Welcome to the game of number guessing!")
print("I have selected a random number between 1 and 100.")

ans = input("Enter the level u want to play (easy, medium, hard): ").lower()


guess_number()
