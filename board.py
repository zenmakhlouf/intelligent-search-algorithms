from cell import Cell
from stone import Stone
class Board:
    def __init__(self,n,goal_pos,red_pos,purple_pos,metal_pos):
        self.n = n
        self.goal_pos = goal_pos
        self.red_pos = red_pos
        self.purple_pos = purple_pos
        self.board = [[Cell("blank","empty") for _ in range(n)] for _ in range(n)]
        for (i,j) in goal_pos:
            self.board[i][j].change_type('goal')
        for(i,j) in red_pos:
           self.board[i][j].put_stone(Stone('red'))
        for (i,j) in purple_pos:
            self.board[i][j].put_stone(Stone("purple"))
        for (i,j) in metal_pos:
             self.board[i][j].put_stone(Stone("metal"))
    
    def can_move(self,new_x,new_y):
        if new_x < 0 or new_y < 0 or new_x >= self.n or new_y >= self.n:
            return False
        return self.board[new_x][new_y].is_empty()
         
    def move_stone(self,old_x,old_y,new_x,new_y):
        if(self.can_move(new_x,new_y)):
            stone = self.board[old_x][old_y].fill
            self.board[old_x][old_y].remove()
            self.board[new_x][new_y].put_stone(stone)
            return self.board

    def display_board(self):
        print("    " + " ".join(f"{i:2}" for i in range(len(self.board))))
        print("  +" + "-" * (len(self.board) * 3 + 1) + "+")
      
        for i, row in enumerate(self.board):
            print(f"{i:2} |", end="")
            for cell in row:
                print(f"{cell.toString():3}", end="")
            print(" |")
        
        print("  +" + "-" * (len(self.board) * 3 + 1) + "+")
    def check_game_over(self):
        for (i,j) in self.goal_pos:
            if self.board[i][j].is_empty():  
                return False                  
        return True 
    def move_purple(self, old_x, old_y, new_x, new_y):
        if not self.can_move(new_x, new_y):
            return False

        self.move_stone(old_x, old_y, new_x, new_y)

       
        for y in range(self.n - 1, new_y, -1):
            if not self.board[new_x][y].is_empty() and self.can_move(new_x, y + 1):
                self.move_stone(new_x, y, new_x, y + 1)

        
        for y in range(0, new_y):
            if not self.board[new_x][y].is_empty() and self.can_move(new_x, y - 1):
                self.move_stone(new_x, y, new_x, y - 1)

        
        for x in range(self.n - 1, new_x, -1):
            if not self.board[x][new_y].is_empty() and self.can_move(x + 1, new_y):
                self.move_stone(x, new_y, x + 1, new_y)

        
        for x in range(0, new_x):
            if not self.board[x][new_y].is_empty() and self.can_move(x - 1, new_y):
                self.move_stone(x, new_y, x - 1, new_y)

        return True
    def move_red(self, old_x, old_y, new_x, new_y):
        
        if not self.can_move(new_x, new_y):
            return False
        
        
        self.move_stone(old_x, old_y, new_x, new_y)
        
        
        for y in range(new_y + 1, self.n):
            if not self.board[new_x][y].is_empty():
                # Found a stone, try to pull it if there's space
                if self.can_move(new_x, y - 1):
                    self.move_stone(new_x, y, new_x, y - 1)
        
        
        for y in range(new_y - 1, -1, -1):
            if not self.board[new_x][y].is_empty():
                if self.can_move(new_x, y + 1):
                    self.move_stone(new_x, y, new_x, y + 1)
        
        
        for x in range(new_x + 1, self.n):
            if not self.board[x][new_y].is_empty():
                if self.can_move(x - 1, new_y):
                    self.move_stone(x, new_y, x - 1, new_y)
        
        
        for x in range(new_x - 1, -1, -1):
            if not self.board[x][new_y].is_empty():
                if self.can_move(x + 1, new_y):
                    self.move_stone(x, new_y, x + 1, new_y)
        
        return True

