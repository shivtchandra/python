import random
alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '=', '+', '[', ']', '{', '}', '|', '\\', ';', ':', '"', "'", '<', '>', ',', '.', '/', '?']

print("Welcome to the Random Password Generator")
n_l = int(input("How Many letters do you want in your password :"))
n_n = int(input("How Mnay Numbers do you want in your password :"))
n_s = int(input("How Many Symbols do you want in your passwprd :"))

password = ""   #This is a password generator but it does the generation in the same sequence as given and no mix up
for p in range (0,n_l):
    password += random.choice(alphabets)
for p in range (0,n_n):
    password += str(random.choice(numbers))
for p in range (0,n_s):
    password += random.choice(symbols)
password_l = list(password)
#A string cannot be shuffled. So We Convert it into a list and do the shuffle 
random.shuffle(password_l)
#print(password) to find out why we need to convert the list bcak to string
password = ''.join(password_l)
print(password)

