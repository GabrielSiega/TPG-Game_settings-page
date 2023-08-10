import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import tkinter.font as tkFont


def Button_6_command():
    print("User pressed Restart")
    
def Button_7_command():
    print("User pressed Exit")

def Button_7_command():
    print("User pressed Exit")
    print()
    print("Settings window & Game Closed")
    root.destroy()
    
def create_text(root, text, x, y):
    label = tk.Label(root, font=tkFont.Font(family='Times', size=10), fg="#333333", justify="center", text=text)
    label.place(x=x, y=y, width=85, height=25)

class Settingspage:
    
    def __init__(self, root):
        self.root = root

        self.audio_on = tk.BooleanVar(value=True)
        self.language = tk.StringVar(value="English")
        self.difficulty_level = tk.DoubleVar(value=1.0)

        self.create_audio_controls()
        self.create_language_dropdown()
        self.create_difficulty_slider()
        self.load_and_display_image()
        self.create_buttons()
        
        

    def create_audio_controls(self):
        audio_label = tk.Label(self.root, text="Audio:", font=("Arial", 12))
        audio_label.place(x=20, y=20)

        audio_on_button = tk.Radiobutton(self.root, text="On", variable=self.audio_on, value=True)
        audio_on_button.place(x=80, y=20)

        audio_off_button = tk.Radiobutton(self.root, text="Off", variable=self.audio_on, value=False)
        audio_off_button.place(x=120, y=20)

    def create_language_dropdown(self):
        language_label = tk.Label(self.root, text="Language:", font=("Arial", 12))
        language_label.place(x=20, y=60)

        languages = ["English", "Spanish", "French", "German"]
        language_dropdown = ttk.Combobox(self.root, textvariable=self.language, values=languages)
        language_dropdown.place(x=120, y=60)

    def create_difficulty_slider(self):
        difficulty_label = tk.Label(self.root, text="Difficulty Level:", font=("Arial", 12))
        difficulty_label.place(x=20, y=100)

        difficulty_slider = tk.Scale(self.root, variable=self.difficulty_level, from_=1, to=10, orient="horizontal")
        difficulty_slider.place(x=150, y=100)

        difficulty_value_label = tk.Label(self.root, textvariable=self.difficulty_level)
        difficulty_value_label.place(x=300, y=100)
        
    def load_and_display_image(self):
        image_path = "C:/TPG Game Zip Files/Game Design/background3.png"  # Replace with the path to your image
        image = Image.open(image_path)
        image = image.resize((200, 200))  # Resize the image if needed
        image_tk = ImageTk.PhotoImage(image)

        image_label = tk.Label(self.root, image=image_tk)
        image_label.place(x=400, y=20)  # Adjust the x and y values as needed
        
    def create_buttons(self):
        button_6 = tk.Button(self.root, text="Restart", font=("Arial", 12), command=Button_6_command)
        button_6.place(x=20, y=160, width=100, height=30)

        button_7 = tk.Button(self.root, text="Exit", font=("Arial", 12), command=Button_7_command)
        button_7.place(x=130, y=160, width=100, height=30)
    
    

        
    


if __name__ == "__main__":
    root = tk.Tk()
    root.title("Settings Page")
    root.geometry("800x600")  # Set the window size to 800x600
    
    print("Settings window opened")
    print()

    game_interface = Settingspage(root)
    root.mainloop()
