# -*- coding: utf-8 -*-

import random

class TicTacToe:
    def __init__(self):
        self.board = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

    def drawBoard(self, board):
        """Draws the passed board. Board is a list of 10 strings.
           Each string represents a position of the board (ignore index 0)"""

        print(' '*7 + board[1] + 4*' ' + '|' + 5*' ' + board[2] + 4*' ' + '|' + 5*' ' + board[3])
        print('  ----------|----------|----------')
        print(' '*7 + board[4] + 4*' ' + '|' + 5*' ' + board[5] + 4*' ' + '|' + 5*' ' + board[6])
        print('  ----------|----------|----------')
        print(' '*7 + board[7] + 4*' ' + '|' + 5*' ' + board[8] + 4*' ' + '|' + 5*' ' + board[9])

    def playAgain(self):
        """Returns True if the player wants to play again, otherwise it returns False."""

        return input('Do you want to play again? (Y for yes): ').lower().startswith('y')

    def makeMove(self, board, letter, index):
        """Places the letter on a board position."""

        board[index] = letter

    def isWinner(self, board, letter):
        """Checks all winning possibilities."""

        firstLineFilled  = board[1] == letter and board[2] == letter and board[3] == letter
        secondLineFilled = board[4] == letter and board[5] == letter and board[6] == letter
        thirdLineFilled  = board[7] == letter and board[8] == letter and board[9] == letter

        firstColumnFilled  = board[1] == letter and board[4] == letter and board[7] == letter
        secondColumnFilled = board[2] == letter and board[5] == letter and board[8] == letter
        thirdColumnFilled  = board[3] == letter and board[6] == letter and board[9] == letter

        mainDiagonalFilled      = board[1] == letter and board[5] == letter and board[9] == letter
        secondaryDiagonalFilled = board[3] == letter and board[5] == letter and board[7] == letter

        return ((firstLineFilled) or (secondLineFilled) or (thirdLineFilled) or
                (firstColumnFilled) or (secondColumnFilled) or (thirdColumnFilled) or
                (mainDiagonalFilled) or (secondaryDiagonalFilled))

    def copyBoard(self, board):
        """Creates a new board as a copy of the passed one."""

        boardCopy = []
        for i in board:
            boardCopy.append(i)

        return boardCopy

    def isSpaceFree(self, board, index):
        """Returns True if position at passed index is empty, otherwise it returns False."""

        if index > 0 and index < 10:
            return not (board[index] == 'X' or board[index] == 'O')
        else:
            return False

    def playerMove(self, board):
        """Enable and check player input."""

        move = " "
        while move not in "1 2 3 4 5 6 7 8 9".split() or not self.isSpaceFree(board, int(move)):
            move = input("What is your next move?")

        return int(move)

    def chooseRandomMoveFromList(self, board, movesList):
        """Takes a free space randomly based on movesList."""

        possibleMoves = []
        for i in movesList:
            if self.isSpaceFree(board, i):
                possibleMoves.append(i)

        if len(possibleMoves) != 0:
            return random.choice(possibleMoves)
        else:
            return None

    def computerMove(self, board, computerLetter):
        """Execute computer input."""

        playerLetter = 'X'

        # Checks if the computer can win next turn
        for i in range(1, 10):
            boardCopy = self.copyBoard(board)
            if self.isSpaceFree(boardCopy, i):
                self.makeMove(boardCopy, computerLetter, i)
                if self.isWinner(boardCopy, computerLetter):
                    return i

        # Checks if the player can win next turn so the computer can block
        for i in range(1, 10):
            boardCopy = self.copyBoard(board)
            if self.isSpaceFree(boardCopy, i):
                self.makeMove(boardCopy, playerLetter, i)
                if self.isWinner(boardCopy, playerLetter):
                    return i

        # Try to take the center, if it is free
        if self.isSpaceFree(board, 5):
            return 5
        else:
            # If the player took the center
            if board[5] == 'X':
                # Try to take one of the corners, if they are free
                move = self.chooseRandomMoveFromList(board, [1, 3, 7, 9])
                if move != None:
                    return move

                # Try to take the center of a line or column
                return self.chooseRandomMoveFromList(board, [2, 4, 6, 8])
            else:
                if not self.isSpaceFree(board, 9) and not self.isSpaceFree(board, 1) and self.isSpaceFree(board, 4):
                    return 4

                if not self.isSpaceFree(board, 9) and not self.isSpaceFree(board, 2) and self.isSpaceFree(board, 3) :
                    return 3

                if  not self.isSpaceFree(board, 1) and not self.isSpaceFree(board, 6) and self.isSpaceFree(board, 2):
                    return 2

                if  not self.isSpaceFree(board, 9) and not self.isSpaceFree(board, 4) and self.isSpaceFree(board, 1):
                    return 1

                if  not self.isSpaceFree(board, 9) and not self.isSpaceFree(board, 4) and self.isSpaceFree(board, 7):
                    return 7

                if  not self.isSpaceFree(board, 8) and not self.isSpaceFree(board, 1) and  self.isSpaceFree(board, 3) :
                    return 7

                if  not self.isSpaceFree(board, 6) and not self.isSpaceFree(board, 7) and self.isSpaceFree(board, 9):
                    return 9

                if  not self.isSpaceFree(board, 2) and not self.isSpaceFree(board, 7) and self.isSpaceFree(board, 4):
                    return 4

                if  not self.isSpaceFree(board, 2) and not self.isSpaceFree(board, 4) and self.isSpaceFree(board, 7):
                    return 7

                if  not self.isSpaceFree(board, 3) and not self.isSpaceFree(board, 7) and self.isSpaceFree(board, 4):
                    return 4

                if  not self.isSpaceFree(board, 3) and not self.isSpaceFree(board, 4) and self.isSpaceFree(board, 7):
                    return 7

                if  not self.isSpaceFree(board, 3) and not self.isSpaceFree(board, 8) and self.isSpaceFree(board, 9):
                    return 9

                if  not self.isSpaceFree(board, 6) and not self.isSpaceFree(board, 8) and self.isSpaceFree(board, 7):
                    return 7

    def isBoardFull(self, board):
        """Checks if all spaces on the board are filled."""

        for i in range(1, 10):
            if self.isSpaceFree(board, i):
                return False

        return True

    def run(self):
        """Runs game logic and game loop."""

        print("Let's play Tic Tac Toe!")
        print("The board:")
        self.drawBoard(self.board)
        print("You can choose any space from 1 to 9!")

        while True:

            self.board = [" "]*10
            playerLetter, computerLetter = ["X", "O"]
            turn = 'player'

            gameIsPlaying = True

            while gameIsPlaying:
                if turn == 'player':
                    print("============================================")
                    print("Player turn:")
                    move = self.playerMove(self.board)
                    self.makeMove(self.board, playerLetter, move)
                    self.drawBoard(self.board)

                    if self.isWinner(self.board, playerLetter):
                        print('Congratulations!!! You won!!!')
                        print('--------------------------------------')
                        gameIsPlaying = False
                    else:
                        if self.isBoardFull(self.board):
                            print('TIE ......')
                            print('--------------------------------------')
                            break
                        else:
                            turn = 'computer'
                else:
                    print("")
                    print("Computer turn:")
                    move = self.computerMove(self.board, computerLetter)
                    self.makeMove(self.board, computerLetter, move)
                    self.drawBoard(self.board)

                    if self.isWinner(self.board, computerLetter):
                        print('Computer Won!!! OMG!!!')
                        print('--------------------------------------')
                        gameIsPlaying = False
                    else:
                        if self.isBoardFull(self.board):
                            print('TIE ......')
                            print('--------------------------------------')
                            break
                        else:
                            turn = 'player'

            if not self.playAgain():
                break
            else:
                print("Let's play again!")
                print("The board:")
                self.board = [" "]*10
                self.drawBoard(self.board)

game = TicTacToe()
game.run()
