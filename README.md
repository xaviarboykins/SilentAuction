# Silent Auction

## Overview
This Python program simulates a **Silent Auction**, where participants anonymously submit their bids, and the highest bidder wins. The program features user inputs to gather bidders and their respective bids, then determines and announces the highest bidder at the end of the auction.

---

## Features
1. **Bidder Management:**
   - Users can enter their names and bid amounts.
   - Multiple bidders can participate in the auction.

2. **Highest Bid Calculation:**
   - The program calculates and announces the highest bid and the winning bidder.

3. **Clear Screen Functionality:**
   - Ensures confidentiality by clearing the screen between bidders.

---

## Requirements
- Python 3.x
- The `art.py` file, which contains the ASCII art logo.

---

## How It Works
1. **Initialization:**
   - The program starts with a welcoming ASCII art logo and an introduction to the silent auction.

2. **Bid Entry:**
   - Each bidder enters their name and bid amount.
   - The bids are stored in a dictionary with bidder names as keys and their bid amounts as values.

3. **Auction Continuation:**
   - After each bid, the user is asked whether there are more bidders.
   - If "yes," the program clears the screen for the next bidder to maintain confidentiality.
   - If "no," the program calculates and announces the winner.

4. **Determine the Winner:**
   - The program iterates through all bids to find and print the highest bidder and their bid amount.

---

## Code Breakdown
### 1. **Functions**
- `add_bidders(bidder_name, bidder_bid)`: Adds a bidder and their bid to the dictionary.
- `calculate_highest_bidder(bid_collection)`: Determines the highest bid and the corresponding bidder, then prints the result.

### 2. **Main Program**
- Initializes an empty `bids` dictionary.
- Uses a `while` loop to collect bids until no more participants are left.
- Calls the appropriate functions to manage bids and calculate the winner.

---

## Setup
1. Ensure both `silent_auction.py` and `art.py` are in the same directory.
2. The `art.py` file should contain a variable `logo` with the desired ASCII art. Example:
   ```python
   logo = '''
   **************************
        SILENT AUCTION
   **************************
   '''
