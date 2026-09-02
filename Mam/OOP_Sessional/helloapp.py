import tkinter as tk

class HelloApp:
    def __init__(self, root):
        self.root = root
        self.root.title("A Greeting System")
        self.root.geometry("800x350")

        # Label
        self.label = tk.Label(self.root, text="Hello! Welcome to this class!", font=("Arial", 20))
        self.label.pack(pady=20)

        # Exit button
        self.exit_button = tk.Button(self.root, text="Exit", font=("Arial", 20), width = 4, height = 1, command=self.close_app)
        self.exit_button.pack()

    def close_app(self):
        self.root.destroy()


# Create the main window
root = tk.Tk()

# Create an object of the class
app = HelloApp(root)

# Start the GUI
root.mainloop()