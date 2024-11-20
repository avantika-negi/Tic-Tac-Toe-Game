import tkinter as tk
from tkinter import messagebox

# Set up the main window
root = tk.Tk()
root.title("Tic Tac Toe")

# Set the background color and window dimensions
root.configure(bg="#add8e6")  # Light blue background
root.geometry("400x400")  # Set the size of the window

# Global variables
current_player = "X"
game_board = [""] * 9
buttons = []

# Switch player
def switch_player():
    global current_player
    current_player = "O" if current_player == "X" else "X"

# Check for a win
def check_win():
    # Winning combinations
    wins = [(0, 1, 2), (3, 4, 5), (6, 7, 8),
            (0, 3, 6), (1, 4, 7), (2, 5, 8),
            (0, 4, 8), (2, 4, 6)]
    
    for a, b, c in wins:
        if game_board[a] == game_board[b] == game_board[c] != "":
            return game_board[a]
    return ""

# Reset the game
def reset_game():
    global game_board, current_player
    game_board = [""] * 9
    current_player = "X"
    for button in buttons:
        button.config(text="", bg="#f0f0f0")  # Reset button color to default

# Button click event
def button_click(idx):
    global game_board
    if game_board[idx] == "":
        game_board[idx] = current_player
        buttons[idx].config(text=current_player, bg="#ffff99")  # Highlight current move with light yellow
        
        winner = check_win()
        if winner:
            messagebox.showinfo("Game Over", f"Player {winner} wins!")
            reset_game()
        elif "" not in game_board:
            messagebox.showinfo("Game Over", "It's a draw!")
            reset_game()
        else:
            switch_player()

# Create buttons
for i in range(9):
    button = tk.Button(
        root,
        text="",
        font=("Arial", 20),
        width=6,
        height=4,
        bg="#f0f0f0",  # Light gray background
        relief="solid",  # Solid border
        bd=1,  # Border width
        command=lambda i=i: button_click(i)
    )
    button.grid(row=i//3, column=i%3, padx=5, pady=5)  # Add spacing between buttons
    buttons.append(button)

root.mainloop()
