import random



famous_people = [
    {"name": "Cristiano Ronaldo", "followers_millions": 625},
    {"name": "Lionel Messi", "followers_millions": 500},
    {"name": "Selena Gomez", "followers_millions": 430},
    {"name": "Kylie Jenner", "followers_millions": 410},
    {"name": "Dwayne Johnson", "followers_millions": 390},
    {"name": "Ariana Grande", "followers_millions": 380},
    {"name": "Kim Kardashian", "followers_millions": 360},
    {"name": "Beyoncé", "followers_millions": 315},
    {"name": "Justin Bieber", "followers_millions": 290},
    {"name": "Taylor Swift", "followers_millions": 270},
]
    # Here we define a function to check if the user is correct or not
    # We take the followers of both the wishes and check if the user is correct or not
def guess_answer(guess, followers_1, followers_2):

    if followers_1> followers_2:
        return guess == "1"
    elif followers_2 > followers_1:
        return guess == "2"

def format(wish):               # Here we define a function to format the wish as we want to repeat it two times
                                #Doing this mutliple times is a waste of time and code
                                # So we define a function to do it for us                            
    wish_name = wish["name"]
    wish_followers = wish["followers_millions"]
    return f" Name : {wish_name} "

print("Welcome to the game!")

game = True
score = 0
wish_2 = random.choice(famous_people)  # Here we choose a random wish from the list of wishes


while game :

    wish_1 = wish_2
    wish_2 = random.choice(famous_people)

    if wish_1 == wish_2:
        wish_2 = random.choice(famous_people)   # Ensure wish_1 and wish_2 are different as they sjouldnt be the same

    print(f"Wish 1: {format(wish_1)}")
    print(" Vs")
    print(f"Wish 2: {format(wish_2)}")

    guess = input("Who has more followers is it 1 or 2?")
    # Here we take input from the user to check if they are correct or not

    followers_1 = wish_1["followers_millions"]
    followers_2 = wish_2["followers_millions"]

    is_correct = guess_answer(guess,followers_1, followers_2)

    # Here we check if the user is correct or not and print the result accordingly

    if is_correct:
        score +=1
        print(f"You are correct! And you score is {score}")

    else:
        print(f"You are wrong! and your score is {score}")
        game = False


