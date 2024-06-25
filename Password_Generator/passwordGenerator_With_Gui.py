import random
import string
import tkinter as tk
from tkinter import messagebox

def check_password_strength(password):
    # Define criteria for a strong password
    length_criteria = len(password) >= 8
    uppercase_criteria = any(char.isupper() for char in password)
    lowercase_criteria = any(char.islower() for char in password)
    digit_criteria = any(char.isdigit() for char in password)
    special_char_criteria = any(char in "!@#$%^&*()-_=+[{]}\|;:'\",<.>/?`~" for char in password)

    # Check if the password meets all criteria
    if length_criteria and uppercase_criteria and lowercase_criteria and digit_criteria and special_char_criteria:
        return "Strong password"
    else:
        # Get the reasons why the password is weak
        reasons = []
        if not length_criteria: reasons.append("Too short (include 8+ characters)")
        if not uppercase_criteria: reasons.append("No uppercase letters")
        if not lowercase_criteria: reasons.append("No lowercase letters")
        if not digit_criteria: reasons.append("No digits")
        if not special_char_criteria: reasons.append("No special chars")

        return "Weak password \nReasons: {}".format(", ".join(reasons))


def password_generator(length):
    # Define the character set
    characters = string.ascii_letters + string.digits + "!@#$%^&*()-_=+[{]}\|;:'\",<.>/?`~"
    # Generate a random password of the specified length
    password = "".join(random.choice(characters) for _ in range(length))
    # Ensure that the password contains uppercase, lowercase, special characters, and digits
    while not (any(char.isupper() for char in password) and any(char.islower() for char in password) and any(char.isdigit() for char in password) and any(char in "!@#$%^&*()-_=+[{]}\|;:'\",<.>/?`~" for char in password)):
        password = "".join(random.choice(characters) for _ in range(length))
    return password


def generate_password():
    length = length_entry.get()
    try:
        length = int(length)
        password = password_generator(length)
        password_output.config(text="Your password is: " + password)
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid length.")


def check_password():
    password = password_entry.get()
    strength = check_password_strength(password)
    strength_output.config(text=strength)


def quit_program():
    window.destroy()


# Create the main window
window = tk.Tk()
window.title("Password Strength Checker and Generator")

# Set window background color
window.configure(bg="#f0f0f0")

# Define styles
label_style = {"font": ("Arial", 12), "bg": "#f0f0f0"}
entry_style = {"font": ("Arial", 12), "bg": "white", "relief": "solid", "borderwidth": 1, "width": 20}
button_style = {"font": ("Arial", 12), "bg": "#4caf50", "fg": "white", "relief": "raised", "borderwidth": 0, "width": 15}

# Create the widgets
length_label = tk.Label(window, text="Enter the length of the password:", **label_style)
length_entry = tk.Entry(window, **entry_style)
generate_button = tk.Button(window, text="Generate Password", command=generate_password, **button_style)
password_output = tk.Label(window, text="", **label_style)
password_label = tk.Label(window, text="Enter the password to check:", **label_style)
password_entry = tk.Entry(window, **entry_style)
check_button = tk.Button(window, text="Check Strength", command=check_password, **button_style)
strength_output = tk.Label(window, text="", **label_style)
quit_button = tk.Button(window, text="Quit", command=quit_program, **button_style)

# Add the widgets to the window
length_label.pack(pady=10)
length_entry.pack(pady=5)
generate_button.pack(pady=10)
password_output.pack(pady=10)
password_label.pack(pady=10)
password_entry.pack(pady=5)
check_button.pack(pady=10)
strength_output.pack(pady=10)
quit_button.pack(pady=10)

# Start the main event loop
window.mainloop()

