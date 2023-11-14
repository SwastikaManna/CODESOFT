import random

def generate_password(length, complexity, excluded_characters):
    """Generates a random password of the specified length, complexity, and excluded characters.
        length: The desired length of the password.
        complexity: The desired complexity of the password.
            "simple": Only lowercase letters and numbers are used.
            "medium": Lowercase and uppercase letters and numbers and four symbols are used.
            "strong": Lowercase and uppercase letters, numbers, and symbols are used.
        excluded_characters: A list of characters to exclude from the password generation algorithm.

    Returns:
        A randomly generated password of the specified length, complexity, and excluded characters.
    """

    characters = []
    if complexity == "simple":
        characters = list("abcdefghijklmnopqrstuvwxyz0123456789")
    elif complexity == "medium":
        characters = list("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!=#@")
    elif complexity == "strong":
        characters = list("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()-~`|_+={}[]|\\;:\'<>,./?")

    for excluded_character in excluded_characters:
        characters.remove(excluded_character)

    password = ""
    for i in range(length):
        password += random.choice(characters)

    return password

def main():
    length = int(input("Enter the desired length of the password: "))
    complexity = input("Choose a complexity level (simple, medium, strong): ")
    excluded_characters = input("Enter any characters to exclude from the password: ")

    password = generate_password(length, complexity, excluded_characters)

    print(f"Your generated password is: {password}")

if __name__ == "__main__":
    main()
