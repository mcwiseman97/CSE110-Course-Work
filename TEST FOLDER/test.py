import curses
import time

def draw_board(stdscr, board):
    stdscr.clear()
    height, width = stdscr.getmaxyx()
    mid_x = width // 2
    mid_y = height // 2

    for y in range(len(board)):
        for x in range(len(board[y])):
            char = 'X' if board[y][x] == 1 else 'O' if board[y][x] == 2 else '.'
            stdscr.addch(y + mid_y, x * 3 + mid_x, char)

    stdscr.refresh()

def get_move(stdscr):
    while True:
        key = stdscr.getch()
        if key in [curses.KEY_LEFT, curses.KEY_RIGHT]:
            return key
        elif key == ord('q'):
            return None

def check_winner(board):
    rows = len(board)
    cols = len(board[0])
    player1 = 1
    player2 = 2

    # Check horizontal
    for y in range(rows):
        for x in range(cols - 3):
            if all(board[y][x + i] == player1 for i in range(4)):
                return player1
            elif all(board[y][x + i] == player2 for i in range(4)):
                return player2

    # Check vertical
    for x in range(cols):
        for y in range(rows - 3):
            if all(board[y + i][x] == player1 for i in range(4)):
                return player1
            elif all(board[y + i][x] == player2 for i in range(4)):
                return player2

    # Check diagonal (top-left to bottom-right)
    for y in range(rows - 3):
        for x in range(cols - 3):
            if all(board[y + i][x + i] == player1 for i in range(4)):
                return player1
            elif all(board[y + i][x + i] == player2 for i in range(4)):
                return player2

    # Check diagonal (top-right to bottom-left)
    for y in range(rows - 3):
        for x in range(3, cols):
            if all(board[y + i][x - i] == player1 for i in range(4)):
                return player1
            elif all(board[y + i][x - i] == player2 for i in range(4)):
                return player2

    # Check for draw
    if any('.' in row for row in board):
        return None
    else:
        return 0

def main(stdscr):
    curses.curs_set(0)  # Hide the cursor
    stdscr.nodelay(1)   # Make getch non-blocking
    stdscr.timeout(100)  # Refresh every 100ms

    rows, cols = 6, 7
    board = [['.' for _ in range(cols)] for _ in range(rows)]
    current_player = 1

    while True:
        draw_board(stdscr, board)
        move = get_move(stdscr)

        if move is None:
            break

        if move == curses.KEY_LEFT:
            # Move left
            pass
        elif move == curses.KEY_RIGHT:
            # Move right
            pass
        else:
            # Drop piece
            for y in range(rows - 1, -1, -1):
                if board[y][current_player - 1] == '.':
                    board[y][current_player - 1] = current_player
                    break

            winner = check_winner(board)
            if winner is not None:
                draw_board(stdscr, board)
                stdscr.addstr(7, 0, f"Player {winner} wins!")
                stdscr.refresh()
                time.sleep(2)
                break

        current_player = 3 - current_player  # Switch player

curses.wrapper(main)
