# TASK 4 ROCK PAPER SCISSORS GAME



import tkinter as tk
from tkinter import messagebox
import random

# Initialize main window
root = tk.Tk()
root.title("Rock-Paper-Scissors Game")
root.geometry("400x400")

# Choices and scores
choices = ["Rock", "Paper", "Scissors"]
user_score = 0
computer_score = 0

# Functions
def play(user_choice):
    global user_score, computer_score
    computer_choice = random.choice(choices)
    
    result_text.set(f"You chose: {user_choice}\nComputer chose: {computer_choice}")
    
    if user_choice == computer_choice:
        outcome.set("It's a Tie!")
    elif (user_choice == "Rock" and computer_choice == "Scissors") or \
         (user_choice == "Scissors" and computer_choice == "Paper") or \
         (user_choice == "Paper" and computer_choice == "Rock"):
        outcome.set("You Win!")
        user_score += 1
    else:
        outcome.set("Computer Wins!")
        computer_score += 1
    
    score.set(f"Score - You: {user_score} | Computer: {computer_score}")

def reset_game():
    global user_score, computer_score
    user_score = 0
    computer_score = 0
    score.set(f"Score - You: {user_score} | Computer: {computer_score}")
    result_text.set("")
    outcome.set("")

# Labels
tk.Label(root, text="Rock-Paper-Scissors", font=("Arial", 18, "bold")).pack(pady=10)

result_text = tk.StringVar()
tk.Label(root, textvariable=result_text, font=("Arial", 12)).pack(pady=10)

outcome = tk.StringVar()
tk.Label(root, textvariable=outcome, font=("Arial", 14, "bold")).pack(pady=5)

score = tk.StringVar()
score.set(f"Score - You: {user_score} | Computer: {computer_score}")
tk.Label(root, textvariable=score, font=("Arial", 12)).pack(pady=5)

# Buttons
button_frame = tk.Frame(root)
button_frame.pack(pady=20)

tk.Button(button_frame, text="Rock", width=10, command=lambda: play("Rock")).grid(row=0, column=0, padx=5)
tk.Button(button_frame, text="Paper", width=10, command=lambda: play("Paper")).grid(row=0, column=1, padx=5)
tk.Button(button_frame, text="Scissors", width=10, command=lambda: play("Scissors")).grid(row=0, column=2, padx=5)

tk.Button(root, text="Reset Game", width=12, command=reset_game).pack(pady=10)

# Run the application
root.mainloop()
