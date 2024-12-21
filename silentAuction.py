import art

def add_bidders(bidder_name, bidder_bid):
    # ADDS BIDDER TO BIDDER DICTIONARY
    bids[bidder_name] = bidder_bid


def calculate_highest_bidder(bid_collection):
    highest_bid = 0
    highest_bidder = ""
    for bidder in bid_collection:
        bid_amount = bid_collection[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            highest_bidder = bidder

    print(f"The highest bidder was {highest_bidder} with a bid of ${highest_bid}.")
    print(f"Congratulations {highest_bidder}, you've won!")




bids = {}
continue_auction = True

print(art.logo)
print("**************************SILENT AUCTION**************************")

while continue_auction:
    name = input("Enter bidder name... \n")
    bid = int(input("Enter bid... \n$"))

    add_bidders(bidder_name=name, bidder_bid=bid)

    continue_answer = input("Are there any more bidders? Type 'yes' or 'no'... \n").lower()

    if continue_answer == "yes":
        print("\n" * 20)

    if continue_answer == "no":
        # calculate the highest bidder
        calculate_highest_bidder(bids)
        continue_auction = False
