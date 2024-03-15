import random
import tkinter as tk
from tkinter import messagebox

class GuessTheNumberGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Guess the Number")
        self.master.geometry("300x200")
        
        self.score = 0
        self.difficulty_options = [
            ("Easy (1-50, 10 attempts)", 1, 50, 10),
            ("Medium (1-100, 7 attempts)", 1, 100, 7),
            ("Hard (1-200, 5 attempts)", 1, 200, 5)
        ]
        
        self.difficulty_var = tk.StringVar()
        self.difficulty_var.set(self.difficulty_options[0][0])
        
        self.difficulty_label = tk.Label(master, text="Select difficulty level:")
        self.difficulty_label.pack()
        
        for text, _, _, _ in self.difficulty_options:
            rb = tk.Radiobutton(master, text=text, variable=self.difficulty_var, value=text)
            rb.pack(anchor=tk.W)
        
        self.start_button = tk.Button(master, text="Start Game", command=self.start_game)
        self.start_button.pack(pady=10)
        
        self.quit_button = tk.Button(master, text="Quit", command=self.quit_game)
        self.quit_button.pack(pady=5)
        
    def start_game(self):
        selected_difficulty = self.difficulty_var.get()
        min_num, max_num, max_attempts = None, None, None
        
        for option in self.difficulty_options:
            if option[0] == selected_difficulty:
                min_num, max_num, max_attempts = option[1:]
                break
        
        secret_number = random.randint(min_num, max_num)
        attempts = 0
        
        while attempts < max_attempts:
            try:
                guess = int(tk.simpledialog.askstring("Guess the Number", "Enter your guess:"))
                
                if guess == secret_number:
                    messagebox.showinfo("Guess the Number", f"Congratulations! You've guessed the number in {attempts + 1} attempts!")
                    self.score += 1
                    break
                elif guess < secret_number:
                    messagebox.showinfo("Guess the Number", "Too low! Try guessing higher.")
                else:
                    messagebox.showinfo("Guess the Number", "Too high! Try guessing lower.")
                
                attempts += 1
                
                if attempts == max_attempts:
                    messagebox.showinfo("Guess the Number", f"You've run out of attempts! The correct number was: {secret_number}")
                    break
            
            except ValueError:
                messagebox.showerror("Error", "Invalid input! Please enter a valid number.")
    
    def quit_game(self):
        self.master.destroy()

def main():
    root = tk.Tk()
    app = GuessTheNumberGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
