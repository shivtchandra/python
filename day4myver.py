import random
print("Hello User")
game = int(input("Now select 0 for Rock or 1 for Paper and 2 for scissors "))
if game == 0 :
 print('''
   _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)''')

elif game == 1 :
 print('''   
   _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)''')
 
elif game == 2 :
 print('''   
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___) ''')
 

list = ["rock","paper","scissor"]

list[0] =   '''
  _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)'''

list[1] = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)'''

list[2] = '''
        _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)'''

print("Computers Choice")
print(random.choice(list))

if game == 0 and list[23]:
 print("win")
elif game == 2 and list[1]:
 print("win")
elif game == 1 and list[0]:
 print("win")
else:
 print("lose")
