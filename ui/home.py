import tkinter as tk
from commands import check_balance
import ui.deposit as deposit_ui


def show_home_ui(root):
    frame = tk.Frame(root, padx=50, pady=50)
    frame.grid(row=0, column=0, sticky="nsew")

    label = tk.Label(frame, text="Please enter account number ")
    label.grid(column=1, row=1)

    entry = tk.Entry(frame, width=50)
    entry.grid(column=2, row=1)

    check_balance_btn = tk.Button(
        frame,
        text="Check Balance",
        command=lambda: check_balance(account_number=entry.get()),
    )
    check_balance_btn.grid(column=3, row=1)

    deposit_btn = tk.Button(
        frame, text="Deposit", command=lambda: deposit_ui.show_deposit_ui(root)
    )
    deposit_btn.grid(column=2, row=2)

    frame.tkraise()
