
import random
import os

def create_board():
    """Creates a dictionary representing the Tic-Tac-Toe board."""
    board = {}
    for row in ['a', 'b', 'c']:
        for col in ['1', '2', '3']:
            board[f"{row}{col}"] = " "
    return board

def display_board(board):
    """Displays the Tic-Tac-Toe board."""
    # Clear the console - simple cross-platform way by printing newlines or using cls/clear
    os.system('cls' if os.name == 'nt' else 'clear') 
    
    print("\n   A   B   C")
    print(" 1 " + board['a1'] + " | " + board['b1'] + " | " + board['c1'])
    print("  ---|---|---")
    print(" 2 " + board['a2'] + " | " + board['b2'] + " | " + board['c2'])
    print("  ---|---|---")
    print(" 3 " + board['a3'] + " | " + board['b3'] + " | " + board['c3'])
    print()

def get_player_names():
    """Gets the names of the two players."""
    print("\nWelcome to the game of Tic Tac Toe!\n")
    player1 = input("What is the first player's name? ").capitalize()
    player2 = input("What is the second player's name? ").capitalize()
    print(f"\nWelcome {player1} and {player2}! Best of luck!\n")
    return [player1, player2]

def check_win(board, symbol):
    """Checks if the given symbol has won."""
    # Horizontal
    if board['a1'] == symbol and board['b1'] == symbol and board['c1'] == symbol: return True
    if board['a2'] == symbol and board['b2'] == symbol and board['c2'] == symbol: return True
    if board['a3'] == symbol and board['b3'] == symbol and board['c3'] == symbol: return True
    
    # Vertical
    if board['a1'] == symbol and board['a2'] == symbol and board['a3'] == symbol: return True
    if board['b1'] == symbol and board['b2'] == symbol and board['b3'] == symbol: return True
    if board['c1'] == symbol and board['c2'] == symbol and board['c3'] == symbol: return True
    
    # Diagonal
    if board['a1'] == symbol and board['b2'] == symbol and board['c3'] == symbol: return True
    if board['c1'] == symbol and board['b2'] == symbol and board['a3'] == symbol: return True
    
    return False

def check_draw(board):
    """Checks if the board is full."""
    for key in board:
        if board[key] == " ":
            return False
    return True

def get_move(player_name, symbol, board):
    """Gets a valid move from the player."""
    while True:
        choice = input(f"{player_name} ({symbol}), choose a cell (e.g. a1): ").lower()
        if choice in board and board[choice] == " ":
            board[choice] = symbol
            return
        elif choice in board:
            print("That cell is already taken. Try again.")
        else:
            print("Invalid cell. Please choose a1, a2, a3, b1, b2, b3, c1, c2, or c3.")

def main():
    board = create_board()
    players = get_player_names()
    
    # Randomly choose who starts
    current_player_index = random.randint(0, 1)
    symbols = ['X', 'O']
    
    print(f"{players[current_player_index]} will go first.")
    input("Press Enter to start...")

    game_on = True
    while game_on:
        display_board(board)
        
        current_player = players[current_player_index]
        current_symbol = symbols[current_player_index]
        
        get_move(current_player, current_symbol, board)
        
        if check_win(board, current_symbol):
            display_board(board)
            print(f"Congratulations! {current_player} wins!")
            game_on = False
        elif check_draw(board):
            display_board(board)
            print("It's a draw!")
            game_on = False
        else:
            # Switch player
            current_player_index = 1 - current_player_index

if __name__ == "__main__":
    main()