print("Welcome To The Tip Calucluator ")
bill = float(input("What was the total bill:"))
tip = int (input("How much tip do u wanto give: 10 12 15 "))
bill = (bill + (bill * tip)/100)
split = int(input("How many persons is the bill gonna be split among:"))
bill = bill / split
bill = round(bill,2)
print(f"Bill per person is gonna be {bill}")