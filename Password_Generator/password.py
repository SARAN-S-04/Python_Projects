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

# Create the widgets
length_label = tk.Label(window, text="Enter the length of the password:")
length_entry = tk.Entry(window)
generate_button = tk.Button(window, text="Generate Password", command=generate_password)
password_output = tk.Label(window, text="")
password_label = tk.Label(window, text="Enter the password to check:")
password_entry = tk.Entry(window)
check_button = tk.Button(window, text="Check Strength", command=check_password)
strength_output = tk.Label(window, text="")
quit_button = tk.Button(window, text="Quit", command=quit_program)

# Add the widgets to the window
length_label.pack()
length_entry.pack()
generate_button.pack()
password_output.pack()
password_label.pack()
password_entry.pack()
check_button.pack()
strength_output.pack()
quit_button.pack()

# Start the main event loop
window.mainloop()
