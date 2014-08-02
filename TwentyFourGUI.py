import tkinter,random,time,re

class TwentyFourGUI:
    wantToPlay = True
    startTime=0
    endTime=0
    
    def __init__(self):
        firstNum=self.getRandomValue()
        secondNum=self.getRandomValue()
        self.numberList = [firstNum,secondNum]
        self.buttonsDisabled=[]
        self.currentDisplay=""

    def getRandomValue(self):
        return random.randint(1,9)

    def addNewValue(self):
        if(self.currentDisplay!=""):
            tkinter.messagebox.showinfo("Can't Add Numbers","You must clear before adding numbers")   
            return
        if(len(self.numberList)==10):
            tkinter.messagebox.showinfo("Too Many Numbers","Ten numbers is the maximum... Try harder to solve using these numbers!")
            return
        newNumber=self.getRandomValue()
        self.numberList.append(newNumber)
        self.updateNumbers()

    def checkAnswer(self,guess):
        if("**" in guess or "%" in guess):
            tkinter.messagebox.showinfo("Invalid","Your expression is invalid")
            return False
        try:
            floatGuess = eval(guess)
            
        except:
            tkinter.messagebox.showinfo("Invalid","Your expression is invalid")
            return False
        
    
        numbersInGuess = re.findall(r"\d+", guess)
        tempList = [""]*len(self.numberList)
        tempList[:] = self.numberList[:]
        
        for number in numbersInGuess:
            if(int(number) in tempList):
                tempList.remove(int(number))
            else:
                tkinter.messagebox.showinfo("Invalid","You used numbers that were not available")
                return False
        if(len(tempList)!=0):
            tkinter.messagebox.showinfo("Invalid","You must use all the available numbers in your answer")
            return False
        
        floatGuess = eval(guess)
        if(floatGuess == 24):
            return True
        else:
            tkinter.messagebox.showinfo("Incorrect","Sorry, your expression does not equal 24. It equals "+ str(floatGuess))
        return False


    def askPlayAgain(self):
        result = tkinter.messagebox.askquestion("Play Again?","Would you like to play again?")
        if result == "yes":
            self.restart()
        else:
            root.destroy()
                                       

    def updateNumbers(self):
        for i in range(len(self.numberList)):
            bttn[i].config(text = "  "+str(self.numberList[i])+"  ")
            bttn[i].config(command = lambda x=self.numberList[i],y=bttn[i]:
                           self.addNumberToBox(str(x),y))

        for i in range(len(self.numberList),len(bttn)):
            bttn[i].config(text = "")
            bttn[i].config(command = lambda:self.resetCommand())
        for i in range(len(self.numberList)):
            bttn[i].config(state=tkinter.NORMAL)
            bttn[i].config(bg="green")
        for button in self.buttonsDisabled:
            button.config(state=tkinter.DISABLED)
            button.config(bg="red")
        
    def printBeginningInstructions(self):
        tkinter.messagebox.showinfo("Rules",
"""Use ALL the numbers in the list exactly once to compute '24'!
You may use '+' to add, '-' to subtract, '*' to multiply, or '/' to divide.
Order of operations is used when computing, so remember to use '()'.
If you want to add another number, please type 'add'.
You can give up and end the game by typing 'quit'""")

    def play(self):
        self.printBeginningInstructions()
        TwentyFourGUI.startTime = time.time()
        self.updateNumbers()
        self.disableSymbols()

    def addOpenParToBox(self):
        self.currentDisplay+="("
        self.display(self.currentDisplay)
        for i in range(len(self.numberList)):
            bttn[i].config(state=tkinter.NORMAL)
        for button in self.buttonsDisabled:
            button.config(state=tkinter.DISABLED)
            button.config(bg="red")
        self.disableSymbols()

    def addClosedParToBox(self):
        self.currentDisplay+=")"
        self.display(self.currentDisplay)
        for i in range(len(self.numberList)):
            bttn[i].config(state=tkinter.DISABLED)
        self.enableSymbols()

    def addSymbolToBox(self,addition):
        self.currentDisplay+=addition
        self.display(self.currentDisplay)
        for i in range(len(self.numberList)):
            bttn[i].config(state=tkinter.NORMAL)
        for button in self.buttonsDisabled:
            button.config(state=tkinter.DISABLED)
            button.config(bg="red")
        self.disableSymbols()

    def disableSymbols(self):
        plus.config(state=tkinter.DISABLED)
        minus.config(state=tkinter.DISABLED)
        mult.config(state=tkinter.DISABLED)
        div.config(state=tkinter.DISABLED)
        equals.config(state=tkinter.DISABLED)

    def enableSymbols(self):
        plus.config(state=tkinter.NORMAL)
        minus.config(state=tkinter.NORMAL)
        mult.config(state=tkinter.NORMAL)
        div.config(state=tkinter.NORMAL)
        equals.config(state=tkinter.NORMAL)
        
    def addNumberToBox(self,addition,button):
        self.currentDisplay+=addition
        self.display(self.currentDisplay)
        for i in range(len(self.numberList)):
            bttn[i].config(state=tkinter.DISABLED)
        button.config(state =tkinter.DISABLED)
        self.buttonsDisabled.append(button)
        button.config(bg="red")
        self.enableSymbols()
        


    def display(self,value):
        text_box.delete(0, tkinter.END)
        text_box.insert(0, value)

    def equals(self):
        inp = self.currentDisplay
        goodAnswer = self.checkAnswer(inp)
        if(goodAnswer == False):
            tkinter.messagebox.showinfo("Incorrect","Please enter another guess or add a number\n")
            self.currentDisplay=""
            self.display(self.currentDisplay)
            self.updateNumbers()
            for i in range(len(self.numberList)):
                bttn[i].config(state=tkinter.NORMAL)
                bttn[i].config(bg="green")
            self.buttonsDisabled=[]
            self.disableSymbols()
        else:
            TwentyFourGUI.endTime = time.time()
            totalGameTime = round(TwentyFourGUI.endTime-TwentyFourGUI.startTime,2)
            tkinter.messagebox.showinfo("You Win!!!", "You used "+ str(len(self.numberList))+" numbers and took "+str(totalGameTime)+" seconds")
            self.askPlayAgain()

    def clear(self):
        self.currentDisplay=""
        self.display(self.currentDisplay)
        self.updateNumbers()
        for i in range(len(self.numberList)):
            bttn[i].config(state=tkinter.NORMAL)
            bttn[i].config(bg="green")
        self.buttonsDisabled=[]
        self.disableSymbols()
        
    def restart(self):
        self.numberList = [self.getRandomValue(),self.getRandomValue()]
        self.updateNumbers()
        self.currentDisplay=""
        self.buttonsDisabled=[]
        self.display(self.currentDisplay)
        TwentyFourGUI.startTime = time.time()
        for i in range(len(self.numberList)):
            bttn[i].config(state=tkinter.NORMAL)
            bttn[i].config(bg="green")
        self.disableSymbols()

    def resetCommand(self):
        pass

game = TwentyFourGUI()
root = tkinter.Tk()
frame = tkinter.Frame(root)
frame.grid()

root.title("Twenty Four")
text_box = tkinter.Entry(frame, justify=tkinter.CENTER, width = 30)
text_box.grid(row = 0, column = 0, columnspan = 5, pady = 5)
text_box.insert(0, "0")

plus = tkinter.Button(frame,text="   +   ",command=lambda: game.addSymbolToBox("+"), justify=tkinter.CENTER)
plus.grid(row = 3, column = 0, pady = 5)

minus = tkinter.Button(frame,text="   -   ",command=lambda: game.addSymbolToBox("-"), justify=tkinter.CENTER)
minus.grid(row = 3, column = 1, pady = 5)

mult = tkinter.Button(frame,text="   *   ",command=lambda: game.addSymbolToBox("*"), justify=tkinter.CENTER)
mult.grid(row = 3, column = 2, pady = 5)

div = tkinter.Button(frame,text=r"   /   ",command=lambda: game.addSymbolToBox(r"/"), justify=tkinter.CENTER)
div.grid(row = 3, column = 3, pady = 5)

equals = tkinter.Button(frame,text="   =   ",command=lambda: game.equals(), justify=tkinter.CENTER)
equals.grid(row = 3, column = 4, pady = 5)


openPar = tkinter.Button(frame,text="   (   ",command=lambda: game.addOpenParToBox(), justify=tkinter.CENTER)
openPar.grid(row = 4, column = 0, pady = 5)

closePar = tkinter.Button(frame,text="   )   ",command=lambda: game.addClosedParToBox(), justify=tkinter.CENTER)
closePar.grid(row = 4, column = 1, pady = 5)

clear = tkinter.Button(frame,text=" clear ",command=lambda: game.clear(), justify=tkinter.CENTER)
clear.grid(row = 4, column = 2, pady = 5)

add = tkinter.Button(frame,text="  add  ",command=lambda: game.addNewValue(), justify=tkinter.CENTER)
add.grid(row = 4, column = 3, pady = 5)

restart = tkinter.Button(frame,text="restart",command=lambda: game.restart(), justify=tkinter.CENTER)
restart.grid(row = 4, column = 4, pady = 5)


i = 0
bttn = []
for j in range(1,3):
    for k in range(0,5):
        bttn.append(tkinter.Button(frame, justify=tkinter.CENTER))
        bttn[i].grid(row = j, column = k, pady = 5)
        i += 1
 
game.play()


root.mainloop()



    
