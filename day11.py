import random

choice =  input("Do you want to play the game :").lower()

def d_cards():
    cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
    card = random.choice(cards)
    return card

def score(cards):

    if 10 in cards and 11 in cards and len(cards) == 2:
        return 0 

    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)

    return sum(cards)

def compare(user_s,computer_s):
    if user_s == computer_s:
         return'Draw'
    elif computer_s == 0:
        return 'lose'
    elif user_s == 0:
        return 'win'
    elif user_s > 21:
        return "win"
    elif computer_s > 21:
        return "lose"
    elif user_s > computer_s:
        return 'win'
    else :
        return "lose"
    


user = []
computer = []
user_score = -1
computer_score = -1
is_gameover = False

for _ in range (2):
    user.append(d_cards())
    computer.append(d_cards())

while not is_gameover:
    user_score = score(user)
    computer_score = score(computer)


    print(f"{user}        {user_score}")
    print(f"{computer[0]}")

    if user_score > 21 or user_score == 0 or computer_score == 0 :
        print("You lose")
        is_gameover = True
    else:
        user_choice = input("Do you want to add another card y or n")
        if user_choice == "y":
            user.append(d_cards())
        else :
            is_gameover = True

while computer_score != 0 and computer_score < 17 :
    computer.append(d_cards())
    computer_score = score(computer)


    print(f"\nYour final hand: {user}, final score: {user_score}")
    print(f"Computer's final hand: {computer}, final score: {computer_score}")
    print(compare(user_score, computer_score))
else:
    print("Maybe next time!")
