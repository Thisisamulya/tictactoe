import random
import emoji
print("\n\nWelcome to Tic Tac Toe \U0001F603")
print("----------------------")
cpossibleNumbers = [1,3,5,7,9]
possibleNumbers = [1,2,3,4,5,6,7,8,9]
gameBoard = [[0,0,0],[0,0,0],[0,0,0]]
rows = 3
cols = 3

def printGameBoard():
  for x in range(rows):
    print("\n+---+---+---+")
    print("|", end="")
    for y in range(cols):
      print("",gameBoard[x][y], end=" |")
  print("\n+---+---+---+")

def modifyArray(num, turn):
  num -= 1
  if(num == 0):
    gameBoard[0][0] = turn
    print(gameBoard[0][0])
  elif(num == 1):
    gameBoard[0][1] = turn
  elif(num == 2):
    gameBoard[0][2] = turn
  elif(num == 3):
    gameBoard[1][0] = turn
  elif(num == 4):
    gameBoard[1][1] = turn
  elif(num == 5):
    gameBoard[1][2] = turn
  elif(num == 6):
    gameBoard[2][0] = turn
  elif(num == 7):
    gameBoard[2][1] = turn
  elif(num == 8):
    gameBoard[2][2] = turn

### Define function to check for a winner
def checkForWinner(gameBoard):
  ### X axis
  if(gameBoard[0][0]+gameBoard[0][1]+gameBoard[0][2] == 15) and gameBoard[0][0]!=0 and gameBoard[0][1]!=0 and gameBoard[0][2]!=0:
    if gameBoard[0][2]%2==0:
      printGameBoard()
      print("you have won! \U0001F389")
    return 0
  elif(gameBoard[0][0]+gameBoard[0][1]+gameBoard[0][2] == 15) and gameBoard[0][0]!=0 and gameBoard[0][1]!=0 and gameBoard[0][2]!=0:
    if gameBoard[0][2]%2!=0:
      printGameBoard()
      print("Computer won!")
    return 0
  elif(gameBoard[1][0]+gameBoard[1][1]+gameBoard[1][2] == 15) and gameBoard[1][0]!=0 and gameBoard[1][1]!=0 and gameBoard[1][2]!=0:
    if gameBoard[1][2]%2==0:
      printGameBoard()
      print("you have won! \U0001F389")
    return 0
  elif(gameBoard[1][0]+gameBoard[1][1]+gameBoard[1][2] == 15) and gameBoard[1][0]!=0 and gameBoard[1][1]!=0 and gameBoard[1][2]!=0:
    if gameBoard[1][2]%2!=0:
      printGameBoard()
      print("Computer won!")
    return 0
  elif(gameBoard[2][0]+gameBoard[2][1]+gameBoard[2][2] == 15) and gameBoard[2][0]!=0 and gameBoard[2][1]!=0 and gameBoard[2][2]!=0:
    if gameBoard[2][2]%2==0:
      printGameBoard()
      print("you have won! \U0001F389")
    return 0
  elif(gameBoard[2][0]+gameBoard[2][1]+gameBoard[2][2] == 15) and gameBoard[2][0]!=0 and gameBoard[2][1]!=0 and gameBoard[2][2]!=0:
    if gameBoard[2][2]%2!=0:
      printGameBoard()
      print("Computer won!")
    return 0
  ### Y axis
  if(gameBoard[0][0]+gameBoard[1][0]+gameBoard[2][0] == 15) and gameBoard[0][0]!=0 and gameBoard[1][0]!=0 and gameBoard[2][0]!=0:
    if gameBoard[2][0]%2==0:
      printGameBoard()
      print("you have won! \U0001F389")
    return 0
  elif(gameBoard[0][0]+gameBoard[1][0]+gameBoard[2][0] == 15) and gameBoard[0][0]!=0 and gameBoard[1][0]!=0 and gameBoard[2][0]!=0:
    if gameBoard[2][0]%2!=0:
      printGameBoard()
      print("Computer won!")
    return 0
  elif(gameBoard[0][1]+gameBoard[1][1]+gameBoard[2][1] == 15) and gameBoard[0][1]!=0 and gameBoard[1][1]!=0 and gameBoard[2][1]!=0:
    if gameBoard[2][1]%2==0:
      printGameBoard()
      print("you have won! \U0001F389")
    return 0
  elif(gameBoard[0][1]+gameBoard[1][1]+gameBoard[2][1] == 15) and gameBoard[0][1]!=0 and gameBoard[1][1]!=0 and gameBoard[2][1]!=0:
    if gameBoard[2][1]%2!=0:
      printGameBoard()
      print("Computer won!")
    return 0
  elif(gameBoard[0][2]+gameBoard[1][2]+gameBoard[2][2] == 15) and gameBoard[0][2]!=0 and gameBoard[1][2]!=0 and gameBoard[2][2]!=0:
    if gameBoard[2][2]%2==0:
      printGameBoard()
      print("you have won! \U0001F389")
    return 0
  elif(gameBoard[0][2]+gameBoard[1][2]+gameBoard[2][2] == 15) and gameBoard[0][2]!=0 and gameBoard[1][2]!=0 and gameBoard[2][2]!=0:
    if gameBoard[2][2]%2!=0:
      printGameBoard()
      print("Computer won!")
    return 0
  ### Cross wins
  elif(gameBoard[0][0]+gameBoard[1][1]+gameBoard[2][2] == 15) and gameBoard[0][0]!=0 and gameBoard[1][1]!=0 and gameBoard[2][2]!=0:
    if gameBoard[2][2]%2==0:
      printGameBoard()
      print("you have won! \U0001F389")
    return 0
  elif(gameBoard[0][0]+gameBoard[1][1]+gameBoard[2][2] == 15) and gameBoard[0][0]!=0 and gameBoard[1][1]!=0 and gameBoard[2][2]!=0:
    if gameBoard[2][2]%2!=0:
      printGameBoard()
      print("Computer won!")
    return 0
  elif(gameBoard[0][2]+gameBoard[1][1]+gameBoard[2][0] == 15) and gameBoard[0][2]!=0 and gameBoard[1][1]!=0 and gameBoard[2][0]!=0:
    if gameBoard[2][0]%2==0:
      printGameBoard()
      print("you have won! \U0001F389")
    return 0
  elif(gameBoard[0][2]+gameBoard[1][1]+gameBoard[2][0] == 15) and gameBoard[0][2]!=0 and gameBoard[1][1]!=0 and gameBoard[2][0]!=0:
    if gameBoard[2][0]%2!=0:
      printGameBoard()
      print("Computer won!")
    return 0
  else:
    return "N"

leaveLoop = False
turnCounter = 0

while(leaveLoop == False):
  ### It's the player turn
  if(turnCounter % 2 == 0):
    printGameBoard()
    print("\U0001F469 your Turn")
    positionPicked = int(input("\nChoose a position to enter number->"))
    pickedNumber= int(input("\nChoose an even number between 1 and 9->"))
    if(positionPicked in possibleNumbers):
      modifyArray(positionPicked, pickedNumber)
      possibleNumbers.remove(positionPicked)
    else:
      print("Invalid input. Please try again.")
    turnCounter += 1
  ### It's the computer's turn
  else:
    while(True):
      cpuChoice = random.choice(possibleNumbers)
      numpicked=random.choice(cpossibleNumbers)
      print("\U0001F4BB AI Turn")
      print("\nComputer chosen position->", cpuChoice)
      print("Computer chose an odd number between 1 and 9->",numpicked)
      if(cpuChoice in possibleNumbers):
        modifyArray(cpuChoice, numpicked)
        possibleNumbers.remove(cpuChoice)
        turnCounter += 1
        break
  
  winner = checkForWinner(gameBoard)
  if(winner != "N"):
    print("\nGame over! Thank you for playing",emoji.emojize(":smiling_face_with_smiling_eyes:"))
    break