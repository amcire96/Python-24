import random, re, time
class TwentyFour:

    wantToPlay = True
    
    def __init__(self):
        self.numberList = [self.getRandomValue(),self.getRandomValue()]

    def getRandomValue(self):
        return random.randint(1,9)

    def addNewValue(self):
        if(len(self.numberList)==10):
            print("Ten numbers is the maximum... Try harder to solve using these numbers!")
            return
        self.numberList.append(self.getRandomValue())
        self.printNumberList()

    def checkAnswer(self,guess):
        if("**" in guess or "%" in guess):
            print("Your expression is invalid")
            return False
        try:
            floatGuess = eval(guess)
            
        except:
            print("Your expression is invalid")
            return False
        
    
        numbersInGuess = re.findall(r"\d+", guess)
        tempList = [""]*len(self.numberList)
        tempList[:] = self.numberList[:]
        
        for number in numbersInGuess:
            if(int(number) in tempList):
                tempList.remove(int(number))
            else:
                print("You used numbers that were not available")
                return False
        if(len(tempList)!=0):
            print("You must use all the available numbers in your answer")
            return False
        
        floatGuess = eval(guess)
        if(floatGuess == 24):
            return True
        else:
            print("Sorry, your expression does not equal 24. It equals", floatGuess)

        return False


    def askPlayAgain(self):
        playAgain = input("Do you want to play again? (Y or N)\n")
        while(playAgain != "Y" and playAgain != "N"):
            playAgain = input("Please use 'Y' or 'N'\n")
        if(playAgain=="Y"):
            TwentyFour.wantToPlay = True
        elif(playAgain=="N"):
            TwentyFour.wantToPlay = False        

    def printNumberList(self):
        print("Numbers: ", self.numberList,"\n")

    def printBeginningInstructions(self):
        print("Use ALL the numbers in the list exactly once to compute '24'!")
        print("You may use '+' to add, '-' to subtract, '*' to multiply, or '/' to divide")  
        print("Order of operations is used when computing, so remember to use parentheses '()'")
        print("If you want to add another number, please type 'add'")
        print("You can give up and end the game by typing 'quit'")

    def play(self):
        self.printBeginningInstructions()

        startTime = time.time()
        
        self.printNumberList()
        
        gameOver = False

    
        while(not gameOver):
              inp = input("")
              if(inp == "add"):
                  self.addNewValue()
              elif(inp == "quit"):
                  gameOver = True
                  print("You quit the game!")
                  self.askPlayAgain()
              else:
                  goodAnswer = self.checkAnswer(inp)
                  if(goodAnswer == False):
                      print("Please enter another guess or add a number\n")
                  else:
                      endTime = time.time()
                      totalGameTime = round(endTime-startTime,2)
                      gameOver = True
                      print("You Win!!! You used", len(self.numberList), "numbers and took", totalGameTime, "seconds")
                      self.askPlayAgain()


while(TwentyFour.wantToPlay):
              
    game = TwentyFour()
    game.play()



