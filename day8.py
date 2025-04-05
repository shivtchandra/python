alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


dir = input("Do You want to encode your message or decode it").lower()
text = input("Enter the Word:")
shift = int(input("Enter the shift :"))

ciph = ""

def ceaser(dir_1,text_1,shift_1):
    cipher = ""
    
    if dir == "decode":
        shift_1 = shift_1 * -1

    for letter in text_1:

        if letter not in alpha:
            cipher += letter

        else:
            og_pos = alpha.index(letter)
            bag = len(alpha)
            og_pos = (og_pos + shift_1) % bag  #These two steps are for conerting the word which is an string into an int value to add the shift value
            #Now we need to convert these numbers back to alphabets
            cipher += alpha[og_pos] #Here cipher is an empty list created to store the alphabets after chabing their index value
    print(f"The {dir_1} word : {cipher}")

ceaser(dir,text,shift)

should = True
while should:
    dog = input("HEY user do u want to continue the game  Yes or No ").lower()
    print(dog)

    if input == "no":
        should = False
    else:
        dir = input("Do You want to encode your message or decode it").lower()
        text = input("Enter the Word:")
        shift = int(input("Enter the shift :"))
        ceaser(dir,text,shift)

   




