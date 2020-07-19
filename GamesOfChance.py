
import random

money = 100

#Function to flip coin
def flip_coin(bet, call):
  num = random.randint(1,2)
  if num == 1 and call == "Heads":
    print("Correct Call")
    print("Amount Won: " + str(bet)) 
    return bet
  elif num == 2 and call == "Tails":
    print("Correct Call")
    print("Amount won: "+ str(bet))
    return bet
  else:
    print("Wrong Call")
    print("Amount lost: -" + str(bet))
    return bet

#Function for Cho-Han
def ChoHan(bet, guess):
  num1 = random.randint(1,6)
  num2 = random.randint(1,6)
  sum = num1 + num2
  if sum % 2 == 0 and guess == "Even":
    print("You guessed Correct!")
    print("Amount Won: " + str(bet))
    return bet
  elif sum % 2 == 1 and guess == "Odd":
    print("You guessed Correct!")
    print("Amount Won:" + str(bet))
    return bet
  else:
    print("You guessed Wrong!")
    print("Amount Lost: -" + str(bet))
    return bet

# Function to pick higher card
def high_card(bet):
  player1_card = random.randint(1,10)
  player2_card = random.randint(1,10)

  if player1_card > player2_card:
    print("Player 1 is the winner!")
    print("Winning Amount: " + str(bet))
    return bet
  elif player2_card > player1_card:
    print("Player 2 is the winner!")
    print("Winning Amount: " + str(bet))
    return bet
  else:
    print("It's a tie, Play again..")
    return bet

# Function to play roulette  
def roulette(bet, guess):
	result = random.randint(0, 37) # We use 37 to represent 00
    if result == 37:
        print("The wheel landed on 00.")
    else:
        print("The wheel landed on " + str(result))
    if guess == "Even" and result % 2 == 0 and result != 0:
        print(str(result) + " is an even number.")
        print("You won " + str(bet)+" dollars!")
        return bet
    elif guess == "Odd" and result % 2 == 1 and result != 37:
        print(str(result) + " is an odd number.")
        print("You won " + str(bet)+" dollars!")
        return bet
    elif guess == result:
        print("You guessed " + str(guess) + " and the result is " + str(result))
        print("You won " + str(bet * 35)+" dollars!")
        return bet * 35
    else:
        print("You lost " + str(bet)+" dollars!")
        return -bet


#Calling the game of chance functions here
money += flip_coin(500, "Heads")
money += ChoHan(200, "Even")
money += high_card(100)
money += roulette(200, "Odd")
print("Your total amount of money is " + str(money))
