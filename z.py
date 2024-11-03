from board import Board
import readchar
import os

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
    #print("\nSelected stone will be marked with '*'")

def main():
    game = Board( #level 1
        4,                     
        [(1, 1), (1, 3)],      
        [],                    
        [(2, 0)],              
        [(1, 2)]               
    )
    # game = Board( #level 2
    #     5,                     
    #     [(2, 0), (0, 2), (2, 2), (4, 2), (2, 4)], 
    #     [],                    
    #     [(3, 0)],              
    #     [(1, 2), (2, 1), (3, 2), (2, 3)]  
    # )
    # game = Board( #level 3
    #     4,
    #     [(0,3),(2,3)],
    #     [],
    #     [(2,0)],
    #     [(1,2)]
    # )
    # game = Board( #level 4
    #     5,
    #     [(0,0),(0,2),(4,1)],
    #     [],
    #     [(2,0)],
    #     [(1,1),(3,1)]
    # )
    # game = Board( level 5
    #     4,
    #     [(0,0),(0,2),(1,0),(1,2),(3,0)],
    #     [],
    #     [(3,1)],
    #     [(1,0),(1,2),(2,0),(2,2)]
    # )
    # game = Board( #level 6
    #     4,
    #     [(0,3),(1,2),(2,3)],
    #     [],
    #     [(2,0)],
    #     [(1,1),(1,3)]

    # )
    # game = Board( #level 7
    #     5,
    #     [(0,0),(1,0),(2,3),(3,2),(4,3)],
    #     [],
    #     [(2,1)],
    #     [(1,0),(2,0),(3,1),(3,2)]
    # )
    # game = Board( #level 8
    #     4,
    #     [(0,0),(0,2),(2,2)],
    #     [],
    #     [(2,0)],
    #     [(1,1),(1,2)]
    # )
    # game = Board( #level 9
    #     7,
    #     [(0,1),(0,3),(0,6)], 
    #     [],
    #     [(0,0)],              
    #     [(0,3),(0,5)]         
    # )
    # game = Board( #level 10
    #     4,
    #     [(1,1),(1,3),(3,0),(3,3)],
    #     [],
    #     [(0,0)],
    #     [(2,2),(2,3),(3,1)]
    # )
    
    # game = Board( #level 11
    #     5,
    #     [(0,1),(0,2),(0,3)],
    #     [(1,2)],
    #     [],
    #     [(0,0),(0,4)]
    # )
    # game = Board( #level 12
    #     5,
    #     [(1,0),(2,0),(4,0),(4,2)],
    #     [(3,1)],
    #     [],
    #     [(0,0),(1,0),(4,3)]
    # )
    # game = Board( #level 13
    #     6,
    #     [(0,3),(0,4),(1,1),(2,1)],
    #     [(2,3)],
    #     [],
    #     [(0,0),(0,4),(0,5)]
    # )
    # game = Board( #level 14
    #     4,
    #     [(1,0),(1,2),(2,1),(2,2)],
    #     [(3,3)],
    #     [],
    #     [(0,3),(2,0),(3,0)]
    # )
    # game = Board( #level 15
    #     5,
    #     [(0,0),(0,2),(1,4),(2,4)],
    #     [(2,2)],
    #     [(1,2)],
    #     [(0,1),(0,3)]
    # )
    # game = Board( level 16
    #     5,                     
    #     [(4, 0), (4, 3), (0, 3), (0, 4)],  
    #     [(2, 0)],              
    #     [(2, 4)],              
    #     [(1, 2), (3, 2)]       
    # )
    # game = Board( #level 17
    #     4,                     
    #     [(1, 1), (3, 1), (2, 2),(1,3)], 
    #     [(0, 0)],              
    #     [(3, 3)],             
    #     [(2, 0), (0, 2)]     
    # )
    # game = Board( #level 18 (doesnt work) because of the law that when there is a space after a stone it stops magnetism
    #    6,
    #    [(1,3),(2,1),(2,2),(2,3),(2,5)],
    #    [(4,2)],
    #    [(4,3)],
    #    [(0,3),(2,0),(2,5)]
    # )
    # game = Board( #level 19
    #    5,
    #    [(1,0),(1,4),(2,1),(3,0),(3,2),(3,4)],
    #    [(2,2)],
    #    [(0,2)],
    #    [(0,1),(0,3),(4,1),(4,3)] 
    # )
    # game = Board( #level 20
    #     5,
    #     [(0,1),(0,3),(1,0),(2,0),(3,0)],
    #     [(4,3)],
    #     [(4,2)],
    #     [(0,1),(0,2),(4,0)]
    # )
    # game = Board( #level 21
    #     4,
    #     [(0,2),(1,0),(1,1),(2,0),(2,1)],
    #     [(2,3)],
    #     [(2,0)],
    #     [(0,1),(1,1),(1,2)]

    # )
    # game = Board( #level 22
    #     5,
    #     [(0,1),(0,3),(1,0),(1,4),(2,1)],
    #     [(3,2)],
    #     [(0,0)],
    #     [(0,3),(0,4),(3,0)]

    # )
    # game = Board( #level 23
    #     5,
    #     [(0,2),(2,1),(2,2),(2,3),(3,2)],
    #     [(3,2)],
    #     [(3,4)],
    #     [(0,3),(1,4),(2,0)]
    # )
    # game = Board( #level 24
    #     5,
    #     [(0,3),(2,1),(2,3),(4,1),(4,2)],
    #     [(3,0)],
    #     [(1,4)],
    #     [(0,1),(1,3),(3,4)]
    # )
    # game = Board( #level 25
    #     5,
    #     [(0,0),(2,0),(4,0),(0,3),(4,1),(4,2)],
    #     [(0,3)],
    #     [(4,0)],
    #     [(0,0),(1,2),(3,2),(4,3)]
       
    # )



    cursor_x, cursor_y = 0, 0
    selected_x, selected_y = None, None
    
    while True:
        clear_screen()
        
        # Display current state
        if selected_x is not None:
            print(f"Selected stone at: ({selected_x}, {selected_y})")
        print(f"Cursor at: ({cursor_x}, {cursor_y})")
        game.display_board()
        print_instructions()

        # Wait for keypress
        key = readchar.readkey()

        if key == 'q':
            break
        
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
            break

if __name__ == "__main__":
    main()
