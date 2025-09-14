import tkinter as tk
import ui.home as home_ui


def show_deposit_ui(root):
    frame = tk.Frame(root, padx=50, pady=50)
    frame.grid(row=0, column=0, sticky="nsew")

    label = tk.Label(frame, text="Please enter deposit amount")
    label.grid(column=1, row=1)

    entry = tk.Entry(frame, width=50)
    entry.grid(column=2, row=1)

    proceed_button = tk.Button(frame, text="Proceed")
    proceed_button.grid(column=3, row=1)

    back_button = tk.Button(
        frame, text="Go Home", command=lambda: home_ui.show_home_ui(root)
    )
    back_button.grid(column=2, row=2)

    frame.tkraise()
