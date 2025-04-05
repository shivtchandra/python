import random
import hangmanlist
import hangmandig

lives = 6


print(hangmandig.hangman_logo)

choosen = random.choice(hangmanlist.word_list)
print(choosen)

place_holder = ""

#w_l = len(choosen)     #This is another method which can be used 
#for position in range(w_l) :
    #place_holder += "_ "
#print(place_holder)

for letter in choosen :
    place_holder += "_ "
print(place_holder)

gameover = False
clist = []

while not gameover:
    guess = (input("Guess a Letter from the word :")).lower()
    print(guess)
    display = ""
    for letter in choosen:
      if letter == guess :
          display += letter
          clist.append(letter)
      elif letter in clist :
          display += letter
      else:
          display = "_ "
    print(display)

    if guess in clist :
        print ("Letter already choosen")
        lives += 0

    if guess not in choosen :
        print (f"{guess}This one is not in the word and u lose a life")
        lives -= 1
        print(f"You have {lives} lifes left in the game ")
        if lives == 0:
            print(f"{choosen} is the right word")
            print("You Lose")

    if "_" not in display :
        gameover = True
        print("You Won")
    
    print(hangmandig.hangman_stages[lives])
