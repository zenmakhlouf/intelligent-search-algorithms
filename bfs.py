from collections import deque
from copy import deepcopy
from stone import Stone

class BFSSolver:
    def __init__(self):
        self.visited = set()
        self.path = []

    def bfs(self, board, max_depth):
        queue = deque([(deepcopy(board), [], 0)])  

        while queue:
            current_board, current_path, current_depth = queue.popleft()

            if current_depth > max_depth:
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

            for stone in stones:
                x, y, stone_type = stone
                for new_x in range(current_board.n):
                    for new_y in range(current_board.n):
                        if (x, y) != (new_x, new_y) and current_board.can_move(new_x, new_y):
                            board_copy = deepcopy(current_board)
                            if stone_type == "purple" and board_copy.move_purple(x, y, new_x, new_y):
                                new_path = current_path + [((x, y), (new_x, new_y))]
                                queue.append((board_copy, new_path, current_depth + 1))
                            elif stone_type == "red" and board_copy.move_red(x, y, new_x, new_y):
                                new_path = current_path + [((x, y), (new_x, new_y))]
                                queue.append((board_copy, new_path, current_depth + 1))

        return False 