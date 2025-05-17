import re
def check_password_strength(password):
    score = 0
    feedback = []

    
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Use at least 8 characters.")

    
    if re.search(r'[A-Z]', password):
        score += 1
    else:
        feedback.append("Add uppercase letters.")

    
    if re.search(r'[a-z]', password):
        score += 1
    else:
        feedback.append("Add lowercase letters.")

    
    if re.search(r'[0-9]', password):
        score += 1
    else:
        feedback.append("Add numbers.")

    
    if re.search(r'[\W_]', password): 
        score += 1
    else:
        feedback.append("Add special characters like !, @, #, etc.")

    if score == 5:
        strength = " is Very Strong"
    elif score >= 3:
        strength = "Moderate"
    else:
        strength = "Weak"

    return strength, feedback


def main():
    password = input("Enter a password to check strength: ")
    strength, feedback = check_password_strength(password)

    print(f"\nPassword Strength: {strength}")
    if feedback:
        print("Suggestions to improve:")
        for f in feedback:
            print("- " + f)

if __name__ == "__main__":
    main()
