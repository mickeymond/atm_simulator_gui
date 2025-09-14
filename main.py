import tkinter as tk
from ui.home import show_home_ui

# Create the main window
root = tk.Tk()

# Add a title to main window
root.title("ATM Simulator")

# Show home ui
show_home_ui(root)

# Open the main window
root.mainloop()
