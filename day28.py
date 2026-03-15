def password_strength(password) -> dict:
    
    if len(password) < 8:
        return {
                "score": 0,
                "label": "Very Weak",
                "reason": "Password must be at least 8 characters long"
            }
    strength = 0
    if len(password) >= 8:
        strength += 1
    if any(char.isdigit() for char in password):
        strength += 1
    if any(char.isupper() for char in password):
        strength += 1
    if any(char.islower() for char in password):
        strength += 1
    if any(char in "!@#$%^&*()-_=+[]{}|;:'\",.<>?/" for char in password):
        strength += 1

    return {
        "score": strength,
        "label": "Very Weak" if strength == 0 else
                 "Weak" if strength == 1 else
                 "Moderate" if strength == 2 else
                 "Strong" if strength == 3 else
                 "Very Strong",
        "reason":"Password is too short" if strength == 0 else
                  "Password lacks complexity" if strength == 1 else
                  "Password could be stronger" if strength == 2 else
                  "Password is strong but could be improved" if strength == 3 else
                  "Password is very strong"
    }


if __name__ == "__main__":
    user_password = input("Enter a password to check its strength:\n")
    result = password_strength(user_password)
    print(f"Password Strength: {result['label']} (Score: {result['score']}/5)")
    print(f"Reason: {result['reason']}")