#PROJECT FOR CODECADEMY COMP-SCI PATH: COIN FLIP
#importing random to randomize result, and time to insert pause between print lines
import random
import time
#global vars that will be used
num = random.randint(1, 10)
bet = ""
result = 0
#making the flip coin function
def coinflip(guess):
    if guess == 1:
        bet = "Heads"
    if guess == 2:
        bet = "Tails"
    result = 0
    if num % 2 == 0:
        result = "Heads"
    else:
        result = "Tails"
    print ("Your Guess is {bet}".format(bet = bet))
    time.sleep(2)
    print("Flipping Coin...")
    time.sleep(2)
    print("Coin dropped, facing on its {result} side".format(result = result))
    time.sleep(2)
    if bet == result:
        print ("You Won")
    else:
        print ("You Lost")
    return
    
#focusing on console output, facing errors like another number or a letter instead of the values i want the user to input
try:
    guess = int(input("Welcome to coinflip game, please press 1 for Heads or 2 for Tails:"))
    if guess < 1 or guess > 2:
        print ("please enter a valid option")
    else:
        coinflip(guess)
except ValueError:
    print ("please enter a valid option")
