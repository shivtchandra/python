menu = {
    "espresso": 
        {
            "ingredients": {
                "water": 50,
                "milk": 0,
                "coffee": 18,
            },
            "cost": 1.5,
        },
    "latte": 
        {
            "ingredients": {
                "water": 200,
                "milk": 150,
                "coffee": 24,
            },
            "cost": 2.5,
        }, 
    "cappuccino": 
        {
            "ingredients": {
                "water": 250,
                "milk": 100,
                "coffee": 24,
            },
            "cost": 3.0,
        }
    
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

cost = {
        "bill" : 0
}

def user_req(ans):
        resources["water"] -= menu[ans]["ingredients"]["water"]
        resources["milk"] -= menu[ans]["ingredients"]["milk"]
        resources["coffee"] -= menu[ans]["ingredients"]["coffee"] 
        cost["bill"] += menu[ans]["cost"] 
        return f"{resources} leffover after making {ans}."

def coins():
     
     ## This function is used to take the coins from the user and calculate the total amount of money inserted
     ## It takes the number of quarters, dimes, nickles and pennies from the user and calculates the total amount of money inserted
     print("Please Insert Coins.")
     total = int(input("How many quarters? ")) * 0.25
     total += int(input("How many dimes? ")) * 0.10
     total += int(input("How many nickles? ")) * 0.05
     total += int(input("How many pennies? ")) * 0.01
     return total



bill = 0
good = True
while good:
    ans = input("What would you like? (espresso/latte/cappuccino): ") 

    if ans == "off":
        good = False
        print("Goodbye!")
    elif ans == "report":
        print(f"Water: {resources["water"]}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${cost['bill']}")
    else:
        if ans in menu:
                
                if resources["water"] >= menu[ans]["ingredients"]["water"] and resources["milk"] >= menu[ans]["ingredients"]["milk"] and resources["coffee"] >= menu[ans]["ingredients"]["coffee"]:
                    total = coins()
                    if total >= menu[ans]["cost"]:
                        change = round(total - menu[ans]["cost"], 2)
                        bill += menu[ans]["cost"]
                        print(f"Here is ${change} in change.")
                        print(f"Here is your {ans} ☕️. Enjoy!")
                        print(user_req(ans))
                        print(f"{bill}")
                    else:
                        print("Sorry that's not enough money. Money refunded.")
                else:
                    print("Sorry there is not enough resources.")
           
    
    