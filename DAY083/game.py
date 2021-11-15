class TicTacToe():
    def __init__(self):
        self.boardDict = {"1": "1", "2": "2", "3": "3"
            , "4": "4", "5": "5", "6": "6"
            , "7": "7", "8": "8", "9": "9"}

    def printBorad(self):
        for key,value in self.boardDict.items():
            if int(key) % 3 == 0:
                print(value)
                print('---------')
            else:
                print(value + ' |', end='\t')
    def createNewBoard(self):
        self.boardDict = {"1": "1", "2": "2", "3": "3"
            , "4": "4", "5": "5", "6": "6"
            , "7": "7", "8": "8", "9": "9"}

    def checkWin(self):
        isWin = False
        if self.boardDict.get('1') == self.boardDict.get('2') == self.boardDict.get('3'):
            isWin=True
        elif self.boardDict.get('4') == self.boardDict.get('5') == self.boardDict.get('6'):
            isWin = True
        elif self.boardDict.get('7') == self.boardDict.get('8') == self.boardDict.get('9'):
            isWin = True
        elif self.boardDict.get('1') == self.boardDict.get('4') == self.boardDict.get('7'):
            isWin = True
        elif self.boardDict.get('2') == self.boardDict.get('5') == self.boardDict.get('8'):
            isWin = True
        elif self.boardDict.get('3') == self.boardDict.get('6') == self.boardDict.get('9'):
            isWin = True
        elif self.boardDict.get('1') == self.boardDict.get('5') == self.boardDict.get('9'):
            isWin = True
        elif self.boardDict.get('3') == self.boardDict.get('5') == self.boardDict.get('7'):
            isWin = True
        return isWin

    def checkTie(self):
        chkValues = list(self.boardDict.values())
        if chkValues.count('O') + chkValues.count('X') == 9:
            print('The game is a tie.')
            return True
        return False

    def quit(self):
        print("Thanks!! Bye~")