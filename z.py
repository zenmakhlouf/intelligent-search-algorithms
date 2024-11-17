from board import Board
import readchar
import os
from dfs import DFSSolver
from copy import deepcopy
from bfs import BFSSolver
from ucs import UCSSolver



def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def get_stone_at(game, x, y):
    if not game.board[x][y].is_empty():
        return game.board[x][y].fill.type
    return None

def print_instructions():
    print("\nControls:")
    print("Arrow keys - Move selection")
    print("Space - Select/Deselect stone")
    print("Q - Quit game")
    print("S - Solve the puzzle using DFS")
    print("B - Solve the puzzle using BFS")
    print("U - Solve the puzzle using UCS")
    #print("\nSelected stone will be marked with '*'")

def select_level():
    levels = [
        (4, [(1, 1), (1, 3)], [], [(2, 0)], [(1, 2)]),  # Level 1
        (5, [(2, 0), (0, 2), (2, 2), (4, 2), (2, 4)], [], [(3, 0)], [(1, 2), (2, 1), (3, 2), (2, 3)]),  # Level 2
        (4, [(0, 3), (2, 3)], [], [(2, 0)], [(1, 2)]),  # Level 3
        (5, [(0, 0), (0, 2), (4, 1)], [], [(2, 0)], [(1, 1), (3, 1)]),  # Level 4
        (4, [(0, 0), (0, 2), (1, 0), (1, 2), (3, 0)], [], [(3, 1)], [(1, 0), (1, 2), (2, 0), (2, 2)]),  # Level 5
        (4, [(0, 3), (1, 2), (2, 3)], [], [(2, 0)], [(1, 1), (1, 3)]),  # Level 6
        (5, [(0, 0), (1, 0), (2, 3), (3, 2), (4, 3)], [], [(2, 1)], [(1, 0), (2, 0), (3, 1), (3, 2)]),  # Level 7
        (4, [(0, 0), (0, 2), (2, 2)], [], [(2, 0)], [(1, 1), (1, 2)]),  # Level 8
        (7, [(0, 1), (0, 3), (0, 6)], [], [(0, 0)], [(0, 3), (0, 5)]),  # Level 9
        (4, [(1, 1), (1, 3), (3, 0), (3, 3)], [], [(0, 0)], [(2, 2), (2, 3), (3, 1)]),  # Level 10
        (5, [(0, 1), (0, 2), (0, 3)], [(1, 2)], [], [(0, 0), (0, 4)]),  # Level 11
        (5, [(1, 0), (2, 0), (4, 0), (4, 2)], [(3, 1)], [], [(0, 0), (1, 0), (4, 3)]),  # Level 12
        (6, [(0, 3), (0, 4), (1, 1), (2, 1)], [(2, 3)], [], [(0, 0), (0, 4), (0, 5)]),  # Level 13
        (4, [(1, 0), (1, 2), (2, 1), (2, 2)], [(3, 3)], [], [(0, 3), (2, 0), (3, 0)]),  # Level 14
        (5, [(0, 0), (0, 2), (1, 4), (2, 4)], [(2, 2)], [(1, 2)], [(0, 1), (0, 3)]),  # Level 15
        (5, [(4, 0), (4, 3), (0, 3), (0, 4)], [(2, 0)], [(2, 4)], [(1, 2), (3, 2)]),  # Level 16
        (4, [(1, 1), (3, 1), (2, 2), (1, 3)], [(0, 0)], [(3, 3)], [(2, 0), (0, 2)]),  # Level 17
        (6, [(1, 3), (2, 1), (2, 2), (2, 3), (2, 5)], [(4, 2)], [(4, 3)], [(0, 3), (2, 0), (2, 5)]),  # Level 18 doesnt work
        (5, [(1, 0), (1, 4), (2, 1), (3, 0), (3, 2), (3, 4)], [(2, 2)], [(0, 2)], [(0, 1), (0, 3), (4, 1), (4, 3)]),  # Level 19
        (5, [(0, 1), (0, 3), (1, 0), (2, 0), (3, 0)], [(4, 3)], [(4, 2)], [(0, 1), (0, 2), (4, 0)]),  # Level 20
        (4, [(0, 2), (1, 0), (1, 1), (2, 0), (2, 1)], [(2, 3)], [(2, 0)], [(0, 1), (1, 1), (1, 2)]),  # Level 21
        (5, [(0, 1), (0, 3), (1, 0), (1, 4), (2, 1)], [(3, 2)], [(0, 0)], [(0, 3), (0, 4), (3, 0)]),  # Level 22
        (5, [(0, 2), (2, 1), (2, 2), (2, 3), (3, 2)], [(3, 2)], [(3, 4)], [(0, 3), (1, 4), (2, 0)]),  # Level 23
        (5, [(0, 3), (2, 1), (2, 3), (4, 1), (4, 2)], [(3, 0)], [(1, 4)], [(0, 1), (1, 3), (3, 4)]),  # Level 24
        (5, [(0, 0), (2, 0), (4, 0), (0, 3), (4, 1), (4, 2)], [(0, 3)], [(4, 0)], [(0, 0), (1, 2), (3, 2), (4, 3)]),  # Level 25
    ]

    print("\nSelect a level:")
   # for i, level in enumerate(levels, start=1):
    #    print(f"{i}. Level {i}")

    choice = int(input("Enter level number: ")) - 1
    return levels[choice]

def main():
    while True:
        level_config = select_level()
        game = Board(*level_config)
        cursor_x, cursor_y = 0, 0
        selected_x, selected_y = None, None
        dfs_solver = DFSSolver()
        bfs_solver = BFSSolver()
        ucs_solver = UCSSolver()
        solution_path = []  # Store the solution path
        no_solution_found = False  # Flag to track if no solution was found
        solution_cost = None

        while True:
            #clear_screen()
            
            # Display current state
            if selected_x is not None:
                print(f"Selected stone at: ({selected_x}, {selected_y})")
            print(f"Cursor at: ({cursor_x}, {cursor_y})")
            game.display_board()
            print_instructions()

            # Print solution if found
            if solution_path:
                print("\nSolution found! Path:")
                if solution_cost:
                    print(f"\n Cost = {solution_cost}")
                for move in solution_path:  # Print in the correct order
                    print(f"Move stone from {move[0]} to {move[1]}")
                no_solution_found = False  # Reset the flag if a solution is found
            elif no_solution_found:
                print("\nNo solution found within the given move limit.")

            # Wait for keypress
            key = readchar.readkey()

            if key == 'q':
                return  # Exit the game
            elif key == 'r':
                break  # Restart the current level
            elif key == 's':
                try:
                    max_depth = input_with_quit("Enter the maximum number of moves allowed: ")
                    if dfs_solver.dfs(deepcopy(game), int(max_depth)):
                        solution_path = dfs_solver.path  # Reverse the path for correct order
                        no_solution_found = False  # Reset the flag if a solution is found
                    else:
                        no_solution_found = True  # Set the flag if no solution is found
                except ValueError:
                    print("\nInvalid input. Please enter a number.")
            elif key == 'b':
                try:
                    max_depth = input_with_quit("Enter the maximum number of moves allowed: ")
                    if bfs_solver.bfs(deepcopy(game), int(max_depth)):
                        solution_path = bfs_solver.path  # BFS path is already in correct order
                        no_solution_found = False  # Reset the flag if a solution is found
                    else:
                        no_solution_found = True  # Set the flag if no solution is found
                except ValueError:
                    print("\nInvalid input. Please enter a number.")
            elif key == 'u':
                try:
                    max_cost = input_with_quit("Enter the maximum cost: ")
                    if ucs_solver.ucs(deepcopy(game),int(max_cost)):
                       solution_path = ucs_solver.path
                       solution_cost = ucs_solver.solution_cost 
                       print("\nUCS Solution found! Cost:", solution_cost)
                       no_solution_found = False
                       
                    else:
                       no_solution_found = True 
                except ValueError:
                    print("\n Invalid input enter a number")
            
            # Handle cursor movement
            if key == '\x1b[A' and cursor_x > 0:  # Up arrow
                cursor_x -= 1
            elif key == '\x1b[B' and cursor_x < game.n - 1:  # Down arrow
                cursor_x += 1
            elif key == '\x1b[D' and cursor_y > 0:  # Left arrow
                cursor_y -= 1
            elif key == '\x1b[C' and cursor_y < game.n - 1:  # Right arrow
                cursor_y += 1
            
            # Handle stone selection/movement
            elif key == ' ':  # Space
                if selected_x is None:
                    # Try to select a stone
                    stone_type = get_stone_at(game, cursor_x, cursor_y)
                    if stone_type in ['red', 'purple']:
                        selected_x, selected_y = cursor_x, cursor_y
                else:
                    # Try to move the selected stone
                    stone_type = get_stone_at(game, selected_x, selected_y)
                    if stone_type == 'red':
                        game.move_red(selected_x, selected_y, cursor_x, cursor_y)
                    elif stone_type == 'purple':
                        game.move_purple(selected_x, selected_y, cursor_x, cursor_y)
                    selected_x, selected_y = None, None

            # Check for win condition
            if game.check_game_over():
                clear_screen()
                game.display_board()
                print("\nCongratulations! You've won!")
                print("Press 'r' to restart, 'q' to quit, or any other key to select a new level.")
                key = readchar.readkey()
                if key == 'r':
                    break  # Restart the current level
                elif key == 'q':
                    return  # Exit the game
                else:
                    break  # Go back to level selection

def input_with_quit(prompt):
    """Custom input function that allows quitting or restarting."""
    while True:
        user_input = input(prompt)
        if user_input.lower() == 'q':
            exit()  # Exit the game
        elif user_input.lower() == 'r':
            raise ValueError("Restart")  # Trigger a restart
        return user_input

if __name__ == "__main__":
    main()
