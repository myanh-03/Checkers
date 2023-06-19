class checkersBoard:
    def __init__ (self):
        self.grid = [[' ',1,  2,  3,  4,  5,  6,  7,  8],
                    ['A',' ','b',' ','b',' ','b',' ','b'],
                    ['B','b',' ','b',' ','b',' ','b',' '],
                    ['C',' ','b',' ','b',' ','b',' ','b'],
                    ['D',' ',' ',' ',' ',' ',' ',' ',' '],
                    ['E',' ',' ',' ',' ',' ',' ',' ',' '],
                    ['F','w',' ','w',' ','w',' ','w',' '],
                    ['G',' ','w',' ','w',' ','w',' ','w'],
                    ['H','w',' ','w',' ','w',' ','w',' '],
                    ]
        self.rowdict = {'A':1,'B':2, 'C':3, 'D':4, 'E':5, 'F':6, 'G':7, 'H':8}
        self.coldict = {'1':1,'2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8}

    def displayBoard (self):
        for row in self.grid :
            # Build up the string for the row
            rowString = ""
            # Loop through the values in the row
            for value in row :
                # Add one value to the string
                rowString = rowString + str(value) + " | "
            # Print out the entire row
            print (rowString)
            print ("-----------------------------------")
    
    def moves (self, currpos, nextpos):
        currRow = currpos[0]
        currCol = currpos[1]
        row = self.rowdict.get(currRow)
        col = self.coldict.get(currCol)
        nextR = nextpos[0]
        nextC = nextpos[1]
        nextRow = self.rowdict.get(nextR)
        nextCol = self.coldict.get(nextC)
        self.grid[nextRow][nextCol] = self.grid[row][col]
        self.grid[row][col] = ' '
        return self.grid

    def capture (self, currpos, nextpos):
        currRow = currpos[0]
        currCol = currpos[1]
        row = self.rowdict.get(currRow)
        col = self.coldict.get(currCol)
        nextR = nextpos[0]
        nextC = nextpos[1]
        nextRow = self.rowdict.get(nextR)
        nextCol = self.coldict.get(nextC)
        if nextRow == (row+2) and nextCol == (col+2) :
                self.grid[row+1][col+1] = ' '
        elif nextRow == (row+2) and nextCol == (col-2) :
                self.grid[row+1][col-1] = ' '
        elif nextRow == (row-2) and nextCol == (col+2) :
                self.grid[row-1][col+1] = ' '
        elif nextRow == (row-2) and nextCol == (col-2) :
                self.grid[row-1][col-1] = ' '
       
        return self.grid
    
    def gameover (self):
        players_dict = {'w': 0, 'b': 0}
        for row in self.grid:
            for column in row:
                if column == 'w':
                    players_dict['w'] = players_dict['w'] + 1
                elif column == 'b':
                    players_dict['b'] = players_dict['b'] + 1

        if players_dict['w'] == 0 :
            b_wins = 'Player "b" wins!:) \n Player "w" loses :('
            return b_wins
        elif players_dict['b'] == 0:
            w_wins = 'Player "w" wins!:) \n Player "b" loses :('
            return w_wins
        else:
            return False

    def checkPositionW(self, currpos):
        currRow = currpos[0]
        currCol = currpos[1]
        row = self.rowdict.get(currRow)
        col = self.coldict.get(currCol)
        if self.grid[row][col] == 'w':
            return True
        else:
            return False

    def checkPositionB(self, currpos):
        currRow = currpos[0]
        currCol = currpos[1]
        row = self.rowdict.get(currRow)
        col = self.coldict.get(currCol)
        if self.grid[row][col] == 'b':
            return True
        else:
            return False
            



#boardcheckers = checkersBoard()
#boardcheckers.displayBoard()
#boardcheckers.moves('F3', 'D5')
#boardcheckers.capture('F3', 'D5')
#boardcheckers.displayBoard()

def main():
    boardcheckers = checkersBoard()
    boardcheckers.displayBoard()
    total_moves = 1000 
    current_piece = ''
    next_move = ''
    user_input = ''
    boardcheckers.gameover()
    while total_moves <= 1000 and user_input != 'quit' and boardcheckers.gameover() == False:
        if total_moves % 2 == 0:
            print("Player 'w', it's your turn" )
            current_piece = input('Type in the place of the piece that you want to move')
            boardcheckers.checkPositionW(current_piece)
            while boardcheckers.checkPositionW(current_piece) == False:
                print("The place you entered doesn't have you piece")
                current_piece = input('Type in the place of the piece that you want to move')
                boardcheckers.checkPositionW(current_piece)
            next_move = input('Type in the place where you want to move the piece')
            boardcheckers.moves(current_piece, next_move)
            boardcheckers.capture(current_piece, next_move)

            boardcheckers.displayBoard()
            boardcheckers.gameover()
            
        else:
            print("Player 'b', it's your turn" )
            current_piece = input('Type in the place of the piece that you want to move')
            boardcheckers.checkPositionB(current_piece)
            while boardcheckers.checkPositionB(current_piece) == False:
                print("The place you entered doesn't have your piece")
                current_piece = input('Type in the place of the piece that you want to move')
                boardcheckers.checkPositionW(current_piece)
            next_move = input('Type in the place where you want to move the piece')
            boardcheckers.moves(current_piece, next_move)
            boardcheckers.capture(current_piece, next_move)
            boardcheckers.displayBoard()
            boardcheckers.gameover()
            
        user_input = input('Type "pass" to continue the game or "quit" to quit the game')
        total_moves = total_moves - 1
    if user_input == 'quit':
        print('The game has ended')
    if boardcheckers.gameover() != False:
        print(boardcheckers.gameover())



main()
        
       


            
    




