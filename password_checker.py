# Project: Simple Password Strength Checker

# Description:
# This project helps users assess the strength of their passwords.
# It checks for length, uppercase, lowercase, digits, and symbols.
# You can run this in any Python environment.

import re

def check_password_strength(password):
    score = 0
    
    # Check length
    if len(password) >= 8:
        score += 1
    
    # Check for uppercase
    if re.search(r"[A-Z]", password):
        score += 1

    # Check for lowercase
    if re.search(r"[a-z]", password):
        score += 1

    # Check for digits
    if re.search(r"\d", password):
        score += 1

    # Check for special characters
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1

    # Evaluate score
    if score == 5:
        return "Very Strong Password"
    elif score == 4:
        return "Strong Password"
    elif score == 3:
        return "Moderate Password"
    elif score == 2:
        return "Weak Password"
    else:
        return "Very Weak Password"

# Main interaction loop
if __name__ == "__main__":
    print("=== Password Strength Checker ===")
    user_password = input("Enter your password: ")
    result = check_password_strength(user_password)
    print("Result:", result)
