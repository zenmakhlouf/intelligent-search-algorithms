from collections import deque
from copy import deepcopy
from stone import Stone


class DFSSolver:
    def __init__(self):
        self.visited = set()
        self.path = []
    
    def dfs(self, board, max_depth):
        stack = [(deepcopy(board), [], 0)]
        
        while stack:
            current_board, current_path, current_depth = stack.pop()
            
            if current_depth > max_depth:
                self.visited.clear()
                continue
            if current_board in self.visited:
                continue
                
            if current_board.check_game_over():
                self.path = current_path
                return True
                
            self.visited.add(deepcopy(current_board))
            
            stones = [(x, y, current_board.board[x][y].fill.type) 
                     for x in range(current_board.n) 
                     for y in range(current_board.n)
                     if isinstance(current_board.board[x][y].fill, Stone) 
                     and current_board.board[x][y].fill.type in ["purple", "red"]]
            
            for x, y, stone_type in stones:
                for new_x in range(current_board.n):
                    for new_y in range(current_board.n):
                        if (x, y) != (new_x, new_y) and current_board.can_move(new_x, new_y):
                            board_copy = deepcopy(current_board)
                            move_successful = False
                            if stone_type == "purple":
                                move_successful = board_copy.move_purple(x, y, new_x, new_y)
                            elif stone_type == "red":
                                move_successful = board_copy.move_red(x, y, new_x, new_y)
                                
                            if move_successful:
                                new_path = current_path + [((x, y), (new_x, new_y))]
                                stack.append((board_copy, new_path, current_depth + 1))
                
        return False