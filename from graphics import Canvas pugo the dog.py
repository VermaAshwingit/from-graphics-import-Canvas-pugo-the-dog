import tkinter as tk

# Constants
CANVAS_WIDTH = 400
CANVAS_HEIGHT = 400
INITIAL_HUNGER = 50
INITIAL_HAPPINESS = 50

class VirtualPet:
    def __init__(self, root):
        self.root = root
        self.root.title("🐾 Meet Pugo, your Virtual Dog!")

        self.canvas = tk.Canvas(root, width=CANVAS_WIDTH, height=CANVAS_HEIGHT, bg='lightblue')
        self.canvas.pack()

        # Initial stats
        self.hunger = INITIAL_HUNGER
        self.happiness = INITIAL_HAPPINESS

        # Draw UI
        self.draw_pet()
        self.draw_stats()
        self.draw_buttons()

    def draw_pet(self):
        self.canvas.delete("pet")
        # Dog face
        self.canvas.create_oval(100, 100, 300, 300, fill='tan', tags="pet")
        # Eyes
        self.canvas.create_oval(150, 150, 170, 170, fill='black', tags="pet")
        self.canvas.create_oval(230, 150, 250, 170, fill='black', tags="pet")

        # Expression
        if self.happiness > 70:
            # Smile
            self.canvas.create_arc(160, 220, 240, 260, start=0, extent=-180, style=tk.ARC, width=3, tags="pet")
        elif self.happiness > 40:
            # Flat mouth
            self.canvas.create_line(170, 240, 230, 240, width=3, tags="pet")
        else:
            # Sad
            self.canvas.create_arc(160, 240, 240, 280, start=0, extent=180, style=tk.ARC, width=3, tags="pet")

    def draw_stats(self):
        self.canvas.delete("stats")
        self.canvas.create_text(200, 20, text="🐶 Pugo the Dog", font=("Arial", 20, "bold"), tags="stats")
        self.canvas.create_text(200, 40, text=f"Hunger: {self.hunger}", font=("Arial", 14), tags="stats")
        self.canvas.create_text(200, 60, text=f"Happiness: {self.happiness}", font=("Arial", 14), tags="stats")

    def draw_buttons(self):
        feed_button = tk.Button(self.root, text="🍖 Feed", command=self.feed_pet)
        feed_button.pack(side=tk.LEFT, padx=40, pady=10)

        play_button = tk.Button(self.root, text="🎾 Play", command=self.play_with_pet)
        play_button.pack(side=tk.RIGHT, padx=40, pady=10)

    def feed_pet(self):
        self.hunger = max(0, self.hunger - 10)
        self.happiness = min(100, self.happiness + 5)
        self.update_display()

    def play_with_pet(self):
        self.happiness = min(100, self.happiness + 10)
        self.hunger = min(100, self.hunger + 5)
        self.update_display()

    def update_display(self):
        self.draw_pet()
        self.draw_stats()

if __name__ == "__main__":
    root = tk.Tk()
    pet = VirtualPet(root)
    root.mainloop()
