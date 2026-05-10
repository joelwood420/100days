def check_password_strength(string):
    if len(string) < 8:
        return "Weak"
    
    has_letters = any(c.isalpha() for c in string)
    has_numbers = any(c.isdigit() for c in string)
    has_upper = any(c.isupper() for c in string)
    has_lower = any(c.islower() for c in string)
    has_special = any(c in "!@#$%^&*." for c in string)
    
    if len(string) >= 10 and has_upper and has_lower and has_numbers and has_special:
        return "Strong"
    
    if len(string) >= 8 and has_letters and has_numbers:
        return "Medium"
    

    return "Weak"

print(check_password_strength("PasSsword1."))
