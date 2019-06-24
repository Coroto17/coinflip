#PROJECT FOR CODECADEMY COMP-SCI PATH #1: COIN FLIP

#importing random to generate a random number to coin flip, and time to insert pause between print lines
import random
import time

#making the flip coin function
def coinflip():
    #local variables, counters
    game_count = 0
    success_count = 0
    print ("Loading Coin Flip...")
    time.sleep(2)
    #encapsulated everything inside a while loop, to make the game start again
    while True:
        #try except block to avoid unwanted inputs (strings), followed by a conditional for checking correct numbers
        try:
            guess = int(input("Please press 1 for Heads or 2 for Tails: "))
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
        play_again = input("enter any key to flip the coin again, or enter \"x\" to exit to the lobby: ")
        if play_again == "x":
            print("Thanks for playing Coin Flip, You Won {success} times out of {total}".format(success=success_count, total=game_count))
            time.sleep(2)
        #the line that exits the game    
            break
        else:
        #the magic line, this continue will redirect to the beginning of the while loop and start the game again    
            continue
    return

#This dice game is a copy paste of coinflip, with proper modifications, expect less comments 
def dice():
    #local variables, counters
    game_count = 0
    success_count = 0
    print ("Loading Dice...")
    time.sleep(2)
    while True:
        try:
            guess = int(input("Please input a number between 1 and 6: "))
        except ValueError:
            print ("please enter a valid option")
            continue
        if guess < 1 or guess > 6:
            print ("please enter a valid number")
            continue
        #using randint to generate the result of throwing
        num = random.randint(1, 6)
        #console output, simulating dice throwing with time sleep
        print ("Your Guess is {guess}".format(guess = guess))
        time.sleep(1)
        print("Throwing dice...")
        time.sleep(2)
        print("Dice finally stops, facing on its {num} side".format(num = num))
        time.sleep(1)
        #checking result to count success and games played
        if guess == num:
            success_count += 1
            print ("You Won")
        else:
            print ("You Lost")
        game_count += 1
        time.sleep(1)
        print ("Game history: correct: {correct} / total {total}".format(correct= success_count, total = game_count))
        time.sleep(2)
        play_again = input("enter any key to throw the dice again, or enter \"x\" to exit to the lobby: ")
        if play_again == "x":
            print("Thanks for playing Dice, You have won {success} times out of {total}".format(success=success_count, total=game_count))
            time.sleep(2)
            break
        else:
            continue
    return
    
#For the final challenge, selecting between 2 games, and letting the user to switch games
while True:
    try:
        game = int(input("Welcome to the game lobby, Press 1 to play Coin Flip, Press 2 to Play Dice, or press 3 to exit: "))
    except ValueError:
        print ("Please enter a valid option")
        continue
    if game == 3:
        print("Thanks for Playing")
        break
    if game < 1 or game > 3:
        print ("Please enter a valid number")
        continue
    else:
        if game == 1:
            coinflip()
            continue
        if game == 2:
            dice()
            continue

