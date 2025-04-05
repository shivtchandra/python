logo = '''  ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\
                         `'-------'`
                       .-------------.
                   jgs/_______________\
'''

print(logo)

print("Hello")

def highest_bid(bid_dic):
    winner = ""
    highest_bid = 0
    for bidder in bid_dic:
        bid_amount = bid_dic[bidder] #Here bidder is the key and the ouput will be an value
        if bid_amount > highest_bid :
            highest_bid = bid_amount
            winner = bidder
    print(f"Winner is {bidder} and the bid amount is {highest_bid}")


dict = {}
bid = True
while  bid :
    key = input("What Is Your Name :")
    value = int(input("How Much Is Your Bid Amount : $"))
    dict[key] = value
    ques = input("Is there anyother person there to bid ?\n").lower()
    print("\n "* 100)
    if ques == "no":
        bid = False
        highest_bid(dict)


