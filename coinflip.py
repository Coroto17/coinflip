#PROJECT FOR CODECADEMY COMP-SCI PATH #1: COIN FLIP

#importing random to generate a random number to coin flip, and time to insert pause between print lines
import random
import time

#making the flip coin function
def coinflip():
    #local variables, counters
    game_count = 0
    success_count = 0
    #encapsulated everything inside a while loop, to make the game start again
    while True:
        #try except block to avoid unwanted inputs (strings), followed by a conditional for checking correct numbers
        try:
            guess = int(input("Welcome to coinflip game, please press 1 for Heads or 2 for Tails: "))
        except ValueError:
            print ("please enter a valid option")
            continue
        if guess < 1 or guess > 2:
            print ("please enter a valid number")
            continue
        #after checking inpput, starts the logic    
        if guess == 1:
            bet = "Heads"
        if guess == 2:
            bet = "Tails"
        #This is where the random flip happens
        num = random.randint(1, 6)
        #depending on the number generated, it will check whether its even or odd, making it a 50% chance.
        if num % 2 == 0:
            result = "Heads"
        else:
            result = "Tails"
        #console output, simulating the flip with time sleep
        print ("Your Guess is {bet}".format(bet = bet))
        time.sleep(2)
        print("Flipping Coin...")
        time.sleep(2)
        print("Coin dropped, facing on its {result} side".format(result = result))
        time.sleep(1)
        #checking result to count success and games played
        if bet == result:
            success_count += 1
            print ("You Won")
        else:
            print ("You Lost")
        game_count += 1
        time.sleep(1)
        #show game history, for the additional challenges section
        print ("Game history: correct: {correct} / total {total}".format(correct= success_count, total = game_count))
        time.sleep(2)
        #this will continue the game or exit in case of x is input
        play_again = input("enter any key to flip the coin again, or enter x to exit: ")
        if play_again == "x":
            print("Thanks for playing")
        #the line that exits the game    
            break
        else:
        #the magic line, this continue will redirect to the beginning of the while loop and start the game again    
            continue
    return
    
#starting coinflip game
coinflip()
