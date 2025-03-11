import math

def print_board(board):
    for row in board:
        print(" ".join(row))
    print()

def check_winner(board):
    for row in board:
        if row[0] == row[1] == row[2] and row[0] != ' ':
            return row[0]
    
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != ' ':
            return board[0][col]
    
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != ' ':
        return board[0][0]
    
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != ' ':
        return board[0][2]
    
    return None

def is_full(board):
    return all(board[r][c] != ' ' for r in range(3) for c in range(3))

def minimax(board, depth, alpha, beta, is_maximizing):
    winner = check_winner(board)
    if winner == 'X':
        return 1
    elif winner == 'O':
        return -1
    elif is_full(board):
        return 0
    
    if is_maximizing:
        max_eval = -math.inf
        for r in range(3):
            for c in range(3):
                if board[r][c] == ' ':
                    board[r][c] = 'X'
                    eval = minimax(board, depth + 1, alpha, beta, False)
                    board[r][c] = ' '
                    max_eval = max(max_eval, eval)
                    alpha = max(alpha, eval)
                    if beta <= alpha:
                        break
        return max_eval
    else:
        min_eval = math.inf
        for r in range(3):
            for c in range(3):
                if board[r][c] == ' ':
                    board[r][c] = 'O'
                    eval = minimax(board, depth + 1, alpha, beta, True)
                    board[r][c] = ' '
                    min_eval = min(min_eval, eval)
                    beta = min(beta, eval)
                    if beta <= alpha:
                        break
        return min_eval

def best_move(board):
    best_val = -math.inf
    move = (-1, -1)
    for r in range(3):
        for c in range(3):
            if board[r][c] == ' ':
                board[r][c] = 'X'
                move_val = minimax(board, 0, -math.inf, math.inf, False)
                board[r][c] = ' '
                if move_val > best_val:
                    best_val = move_val
                    move = (r, c)
    return move

def play_game():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    print("Noughts and Crosses: AI (X) vs. Human (O)")
    print_board(board)
    
    while True:
        if is_full(board) or check_winner(board):
            break
        
        row, col = best_move(board)
        board[row][col] = 'X'
        print("AI chooses:")
        print_board(board)
        
        if check_winner(board) or is_full(board):
            break
        
        while True:
            try:
                user_row, user_col = map(int, input("Enter row and column (0-2) separated by space: ").split())
                if board[user_row][user_col] == ' ':
                    board[user_row][user_col] = 'O'
                    break
                else:
                    print("Invalid move, try again.")
            except (ValueError, IndexError):
                print("Invalid input, enter numbers between 0 and 2.")
        print_board(board)
    
    winner = check_winner(board)
    if winner:
        print(f"{winner} wins!")
    else:
        print("It's a draw!")

if __name__ == "__main__":
    play_game()
