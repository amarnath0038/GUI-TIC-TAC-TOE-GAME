import tkinter as tk
from tkinter import messagebox

def check_winner(board):
    for player in ['X', 'O']:
        if (board[0][0] == board[0][1] == board[0][2] == player or
            board[1][0] == board[1][1] == board[1][2] == player or
            board[2][0] == board[2][1] == board[2][2] == player or
            board[0][0] == board[1][0] == board[2][0] == player or
            board[0][1] == board[1][1] == board[2][1] == player or
            board[0][2] == board[1][2] == board[2][2] == player or
            board[0][0] == board[1][1] == board[2][2] == player or
            board[0][2] == board[1][1] == board[2][0] == player):
            return player
    return None

def print_board():
    for i in range(3):
        for j in range(3):
            button_grid[i][j].config(text=board[i][j])

def on_click(row, col):
    global turn, board
    if board[row][col] == ' ':
        board[row][col] = turn
        print_board()
        
        winner = check_winner(board)
        if winner:
            messagebox.showinfo("Game Over", f"Player {winner} wins!")
            root.quit()
        elif all(all(cell != ' ' for cell in row) for row in board):
            messagebox.showinfo("Game Over", "It's a draw!")
            root.quit()
        else:
            turn = 'O' if turn == 'X' else 'X'

root = tk.Tk()
root.title("Tic Tac Toe")

# Setting window size (optional)
root.geometry("300x300")

board = [[' ' for _ in range(3)] for _ in range(3)]
turn = 'X'

button_grid = [[None for _ in range(3)] for _ in range(3)]
for i in range(3):
    for j in range(3):
        button_grid[i][j] = tk.Button(root, text=' ', width=10, height=4,
                                      command=lambda row=i, col=j: on_click(row, col))
        button_grid[i][j].grid(row=i, column=j)

root.mainloop()
