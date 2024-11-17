from queue import PriorityQueue
from copy import deepcopy
from stone import Stone
import logging

# Setup logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class UCSSolver:
    def __init__(self):
        self.visited = set()
        self.path = []
        self.solution_cost= None

    def ucs(self, board, max_cost):
        logger.info("Starting UCS with a max cost of %s", max_cost)
        queue = PriorityQueue()
        start_board_id = id(board)
        queue.put((0, start_board_id, deepcopy(board), []))  # (cost, board id, board, path)
        logger.debug("Initial board state added to queue with cost 0")

        while not queue.empty():
            current_cost, current_board_id, current_board, current_path = queue.get()
            logger.debug("Dequeuing item with cost %s, board id %s", current_cost, current_board_id)

            if current_cost > max_cost:
                logger.info("Current cost %s exceeds max cost %s, skipping this state", current_cost, max_cost)
                continue
            
            board_hash = hash(tuple(tuple(cell.toString() for cell in row) for row in current_board.board))
            logger.debug("Checking if board state %s has been visited", board_hash)

            if board_hash in self.visited:
                logger.debug("Board state %s already visited, skipping", board_hash)
                continue
            
            if current_board.check_game_over():
                logger.info("Solution found with path: %s", current_path)
                self.path = current_path
                self.solution_cost = current_cost
                return True
            
            self.visited.add(board_hash)
            logger.debug("Board state %s added to visited set", board_hash)

            stones = [(x, y, current_board.board[x][y].fill.type)
                      for x in range(current_board.n)
                      for y in range(current_board.n)
                      if isinstance(current_board.board[x][y].fill, Stone)
                      and current_board.board[x][y].fill.type in ["purple", "red"]]
            
            logger.debug("Found %s movable stones", len(stones))

            for stone in stones:
                x, y, stone_type = stone
                for new_x in range(current_board.n):
                    for new_y in range(current_board.n):
                        if (x, y) != (new_x, new_y) and current_board.can_move(new_x, new_y):
                            logger.debug("Considering move: (%s, %s) -> (%s, %s) for %s stone", 
                                         x, y, new_x, new_y, stone_type)
                            board_copy = deepcopy(current_board)
                            move_cost = board_copy.calc_move_cost(x, y, new_x, new_y, stone_type)

                            if stone_type == "purple" and board_copy.move_purple(x, y, new_x, new_y):
                                new_path = current_path +[((x, y), (new_x, new_y))]
                                new_board_hash = hash(tuple(tuple(cell.toString() for cell in row) for row in board_copy.board))
                                queue.put((current_cost + move_cost, id(board_copy), board_copy, new_path))
                                logger.debug("Added purple move to queue. New cost: %s, New board hash: %s", 
                                             current_cost + move_cost, new_board_hash)
                            elif stone_type == "red" and board_copy.move_red(x, y, new_x, new_y):
                                new_path = current_path +[((x, y), (new_x, new_y))]
                                new_board_hash = hash(tuple(tuple(cell.toString() for cell in row) for row in board_copy.board))
                                queue.put((current_cost + move_cost, id(board_copy), board_copy, new_path))
                                logger.debug("Added red move to queue. New cost: %s, New board hash: %s", 
                                             current_cost + move_cost, new_board_hash)

        logger.info("UCS did not find a solution within the cost limit")
        return False