from tkinter import messagebox
import csv

def check_balance(account_number):
    # Open the csv file
    csv_file = open(file="accounts.csv", mode="r")
    # Read the csv content
    accounts = csv.DictReader(csv_file)
    for account in accounts:
        if account_number == account["account_number"]:
            # Show balance with message box
            messagebox.showinfo(
                title="Check Balance",
                message=f"Your balance is {account["balance"]}")
            return
    # Show user an acoount not found message
    messagebox.showerror(
        title="Check Balance",
        message=f"Account number {account_number} does not exist!")