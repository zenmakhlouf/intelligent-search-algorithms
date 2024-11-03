from copy import deepcopy


class Dfs:
    def __init__(self,board):
        visited = []
        path = []
        self.board = board
    
    def get_possible_purple_moves(self):
        possible_moves_coords = []
        for (i,j) in self.board.purple_pos:
            for(i,j) in self.board:
                if self.board[i][j].is_empty:
                    possible_moves_coords.append((i,j))
    def dfs(self,board):
        current_state = self.board
        if current_state in self.visited:
            return False
        if current_state.check_game_over():
            return True
        self.visited.add(current_state)

        purple_stones = self.board.purple_pos
        for stone_pos in purple_stones:
            x,y = stone_pos
            for new_x in range(self.board.n):
                for new_y in range(self.board.n):
                    board_copy = deepcopy(current_state)
                    if stone_pos in purple_stones:
                        move = self.board.move_purple(x,y,new_x,new_y)
                    if move and self.dfs(board_copy):
                        self.path.append((stone_pos, (new_x, new_y)))
                        return True
                    
        return False



        

