
def add(n1, n2):
    return n1+n2
def subtract(n1,n2):
    return n1-n2
def multpily(n1,n2):
    return n1*n2
def divide(n1,n2):
    return n1/n2



calc = {
    "+" : add,
    "-" : subtract,
    "*" : multpily,
    "/" : divide,
}

def cal():
    n1 = float(input("NUM1 :"))

    cont = True

    while cont :
        operator = input("Enter the operator:")
        n2 = float(input("NUM2 :"))
        ans = calc[operator](n1,n2)
        print(f"{n1} {operator} {n2} = {ans}")
        choice = input(f"If You wanna perform more operations on {ans} then types yes or go with no if not").lower()
        if choice == "yes":
            n1 = ans     
        elif choice == "no":
            cont = False
            cal()

cal()
