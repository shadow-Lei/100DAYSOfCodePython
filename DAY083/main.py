from game import TicTacToe
'''
Tic Tac Toe 圈圈叉叉
'''


if __name__ == "__main__":
    continueGameYN = input('Do you want to play the Tic Tac Toe?(Y or N)')
    game = TicTacToe()
    while continueGameYN.upper() == 'Y':
        nowPlayer = 'X'
        isGameOver = False
        game.createNewBoard()

        game.printBorad()
        while not isGameOver:
            nowPlayerPoint = input(f'turn to player ({nowPlayer}) :')
            if not game.boardDict.get(nowPlayerPoint) or game.boardDict.get(nowPlayerPoint)!=str(nowPlayerPoint):
                print('Please input again')
            else:
                game.boardDict[str(nowPlayerPoint)]=nowPlayer
                game.printBorad()
                isWin=game.checkWin()
                if isWin:
                    print(nowPlayer + ' is winner!!')
                    break
                isTie=game.checkTie()
                if isTie:
                    break
                nowPlayer = 'X' if nowPlayer == 'O' else "O"

        continueGameYN = input('Do you want to play the Tic Tac Toe?(Y or N)')
    game.quit()
