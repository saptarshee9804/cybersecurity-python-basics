
def check_password_strength(password):
    score = 0

    if len(password) >= 12:
        score += 1

    if any(char.islower() for char in password):
        score += 1

    if any(char.isupper() for char in password):
        score += 1

    if any(char.isdigit() for char in password):
        score += 1

    if any(not char.isalnum() for char in password):
        score += 1

    if score <= 2:
        return "Needs improvement"
    elif score <= 4:
        return "Moderate"
    else:
        return "Meets the basic checks"


# Use a fictional example only.
example = "ExamplePass123!"
print(check_password_strength(example))
