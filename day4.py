import random
rock = ('''   '
'' _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)'''
)

paper = ('''  
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)''')

scissors = ('''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)''')

game = [rock,paper,scissors]

user = int(input("choose 0 for rock , 1 for paper and 2 for scissor"))

if 0 <= user <= 2:
    print(game[user])
computer = random.randint(0,2)
print("computer choice:")
print(game[computer])

if user >= 3 or user < 0 :
    print("Invalid Number")
elif user == 0 and computer == 2:
    print("You Win")
elif user == 2 and computer == 0:
    print("lose")
elif user > computer :
    print("you win")
#elif user == 1 and computer == 0 :
    #print("win")
#elif user == 2 and computer == 1:
    #print("win")
elif user == computer :
    print("Draw")
#elif user == 0 and computer == 1 :
    #print("lose")
#elif user == 1 and computer == 2:
    #print("lose")
elif computer > user :
    print("lose")