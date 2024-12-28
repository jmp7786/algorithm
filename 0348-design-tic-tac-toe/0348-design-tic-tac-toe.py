class TicTacToe:

    def __init__(self, n: int):
        self.board = [[0]*n for i in range(n)]
        self.size = n

    def move(self, row: int, col: int, player: int) -> int:
        self.board[row][col] = player
        result = self._check_win(row,col,player)
        if result:
            return player
        return 0

    def _check_win(self, row: int, col: int, player: int) -> bool: 
        # print(row, col, player)
        count = 0
        for i in range(self.size): 
            if self.board[row][i] == player: 
                # print(3)
                count = count + 1
                # print(count,-1)
        
        if count == self.size: 
            return True 
        # print(count)
        count = 0
        for i in range(self.size): 
            if self.board[i][col] == player: 
                count = count + 1
        if count == self.size: 
            return True 
        
        if col == row: 
            count = 0
            for i in range(self.size): 
                if self.board[i][i] == player: 
                    count = count + 1
            if count == self.size: 
                return True 
        
        if col + row == self.size-1: 
            count = 0
            for i in range(self.size): 
                if self.board[self.size-1-i][i] == player: 
                    count = count + 1
            if count == self.size: 
                return True 

        return False
        
        
    
        
# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)