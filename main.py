from replit import clear
from art import logo
print(logo)
print('Welcome to the secret auction Program.')

should_continue = True
bidders = {}
highest_bids = []
highest_bidder = ''
while should_continue:
    name = input("What is your name?: ")
    bid = int(input("What is your bid?: $"))
    another_bid = input('Are there any other bidders? Type yes or no.\n ')
    bidders[name] = bid
    highest_bids.append(bidders[name])
    highest_bid = max(highest_bids)
    for key, val in bidders.items():
           if highest_bid == val:
               highest_bidder = key
    
    if another_bid == 'no':
        should_continue = False
        clear()
        print(f"The highest bidder is {highest_bidder} with a bid of ${highest_bid}.")
    else:
        clear()
  