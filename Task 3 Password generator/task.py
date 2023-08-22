import random
import string

def generate_password(length, strength):
    if strength == "easy":
        characters = string.ascii_letters + string.digits
    elif strength == "medium":
        characters = string.ascii_letters + string.digits + string.punctuation
    elif strength == "complex":
        characters = string.ascii_letters + string.digits + string.punctuation + string.ascii_uppercase + string.punctuation
    else:
        raise ValueError("Invalid strength level")

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("Welcome to the Password Generator!")
    try:
        password_length = int(input("Enter the desired length of the password: "))
        if password_length <= 0:
            print("Password length must be greater than 0.")
            return

        print("Select password strength:")
        print("Press 'e' for Easy")
        print("Press 'm' for Medium")
        print("Press 'c' for Complex")

        strength_choice = input("Enter your choice: ").lower()
        if strength_choice == 'e':
            strength = "easy"
        elif strength_choice == 'm':
            strength = "medium"
        elif strength_choice == 'c':
            strength = "complex"
        else:
            print("Invalid choice. Please select a valid option.")
            return

        generated_password = generate_password(password_length, strength)
        print("Generated Password:", generated_password)
    except ValueError:
        print("Invalid input. Please enter valid values.")

if __name__ == "__main__":
    main()
