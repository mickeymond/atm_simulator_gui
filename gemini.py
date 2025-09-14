import tkinter as tk
from tkinter import ttk

def create_main_window():
    """Sets up the main window and its properties."""
    root = tk.Tk()
    root.title("ATM")
    root.geometry("800x600")
    root.configure(bg="#1E2A78")
    return root

def create_ui(root):
    """Builds all the widgets for the ATM UI."""
    # Main frame for the content
    main_frame = tk.Frame(root, bg="#1E2A78")
    main_frame.pack(fill="both", expand=True, padx=20, pady=20)

    # Top bar
    create_top_bar(main_frame)

    # Content frame
    content_frame = tk.Frame(main_frame, bg="#1E2A78")
    content_frame.pack(fill="both", expand=True)

    # Left side panel for user info
    create_info_panel(content_frame)

    # Right side for button grid
    create_button_grid(content_frame)

    # Quick Cash section
    create_quick_cash_section(main_frame)

def create_top_bar(parent):
    """Creates the ATM and Card Return labels at the top."""
    top_frame = tk.Frame(parent, bg="#1E2A78")
    top_frame.pack(fill="x")

    tk.Label(top_frame, text="ATM", font=("Helvetica", 24, "bold"), fg="white", bg="#1E2A78").pack(side="left", padx=10, pady=10)
    tk.Label(top_frame, text="Card Return", font=("Helvetica", 14), fg="white", bg="#1E2A78").pack(side="right", padx=10, pady=10)

def create_info_panel(parent):
    """Creates the user information panel on the left."""
    info_frame = tk.Frame(parent, bg="#1E2A78")
    info_frame.pack(side="left", fill="y", padx=20, pady=20)

    tk.Label(info_frame, text="Welcome", font=("Helvetica", 12), fg="#B8B8FF", bg="#1E2A78").pack(anchor="w", pady=(0, 5))
    tk.Label(info_frame, text="Steph Curry", font=("Helvetica", 20, "bold"), fg="white", bg="#1E2A78").pack(anchor="w", pady=(0, 20))
    tk.Label(info_frame, text="Account #1", font=("Helvetica", 12), fg="#B8B8FF", bg="#1E2A78").pack(anchor="w", pady=(0, 5))
    tk.Label(info_frame, text="$2.380", font=("Helvetica", 28, "bold"), fg="white", bg="#1E2A78").pack(anchor="w", pady=(0, 20))
    tk.Label(info_frame, text="Savings #2", font=("Helvetica", 12), fg="#B8B8FF", bg="#1E2A78").pack(anchor="w", pady=(0, 5))
    tk.Label(info_frame, text="$795", font=("Helvetica", 28, "bold"), fg="white", bg="#1E2A78").pack(anchor="w")

def create_button_grid(parent):
    """Creates the 3x2 grid of action buttons."""
    buttons_frame = tk.Frame(parent, bg="#1E2A78")
    buttons_frame.pack(side="right", fill="both", expand=True, padx=20, pady=20)

    buttons_frame.grid_columnconfigure(0, weight=1)
    buttons_frame.grid_columnconfigure(1, weight=1)
    buttons_frame.grid_rowconfigure(0, weight=1)
    buttons_frame.grid_rowconfigure(1, weight=1)
    buttons_frame.grid_rowconfigure(2, weight=1)

    def create_action_button(parent, text, color="#2E69E8"):
        """A helper function to create a stylized button."""
        return tk.Button(parent, text=text, font=("Helvetica", 16), fg="white", bg=color, relief="flat", bd=0)

    create_action_button(buttons_frame, "Get Cash").grid(row=0, column=0, sticky="nsew", padx=10, pady=10)
    create_action_button(buttons_frame, "Deposit").grid(row=0, column=1, sticky="nsew", padx=10, pady=10)
    create_action_button(buttons_frame, "Payments").grid(row=1, column=0, sticky="nsew", padx=10, pady=10)
    create_action_button(buttons_frame, "Credit Card").grid(row=1, column=1, sticky="nsew", padx=10, pady=10)
    create_action_button(buttons_frame, "Account Settings").grid(row=2, column=0, sticky="nsew", padx=10, pady=10)
    create_action_button(buttons_frame, "Other", color="#1E2A78").grid(row=2, column=1, sticky="nsew", padx=10, pady=10)

def create_quick_cash_section(parent):
    """Creates the 'Quick Cash' button at the bottom."""
    quick_cash_frame = tk.Frame(parent, bg="#FF005E", height=80)
    quick_cash_frame.pack(fill="x", pady=(20, 0))
    quick_cash_frame.pack_propagate(False)

    tk.Label(quick_cash_frame, text="$70", font=("Helvetica", 24, "bold"), fg="white", bg="#FF005E").pack(side="left", padx=20, pady=10)
    tk.Label(quick_cash_frame, text="Quick Cash", font=("Helvetica", 18), fg="white", bg="#FF005E").pack(side="left", padx=10)
    tk.Label(quick_cash_frame, text=">", font=("Helvetica", 24, "bold"), fg="white", bg="#FF005E").pack(side="right", padx=20)

# Main execution block
if __name__ == "__main__":
    main_window = create_main_window()
    create_ui(main_window)
    main_window.mainloop()