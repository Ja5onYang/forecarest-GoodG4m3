import tkinter as tk
import random

class Lottery:
    def __init__(self):
        self.score = 0
        self.prizes = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L']
        self.window = tk.Tk()
        self.window.title("Lottery")

        # Center the window
        window_width = 500
        window_height = 200
        screen_width = self.window.winfo_screenwidth()
        screen_height = self.window.winfo_screenheight()
        position_top = int(screen_height / 2 - window_height / 2)
        position_right = int(screen_width / 2 - window_width / 2)
        self.window.geometry(f"{window_width}x{window_height}+{position_right}+{position_top}")

        self.entry = tk.Entry(self.window)
        self.entry.bind('<Return>', self.add_score)
        self.entry.pack()

        self.score_label = tk.Label(self.window, text="Score: 0")
        self.score_label.pack()

        self.prize_labels = []
        for prize in self.prizes:
            label = tk.Label(self.window, text=prize)
            label.pack(side=tk.LEFT)
            self.prize_labels.append(label)

        self.button = tk.Button(self.window, text="draw!", command=self.draw_lottery)
        self.button.pack()

        self.window.mainloop()

    def add_score(self, event):
        self.score += 1
        self.score_label.config(text=f"Score: {self.score}")
        self.entry.delete(0, 'end')  # Clear the entry field

    def draw_lottery(self):
        if self.score >= 10:
            self.score -= 10
            self.score_label.config(text=f"Score: {self.score}")
            prize = random.choice(self.prizes)
            for label in self.prize_labels:
                if label.cget("text") == prize:
                    label.config(fg="red")
                else:
                    label.config(fg="black")
        else:
            print("Not enough!")

if __name__ == "__main__":
    Lottery()

