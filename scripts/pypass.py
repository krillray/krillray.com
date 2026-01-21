"""
This module provides a password generator tool called PyPass.

Functions:
- generate_password: Generates a password based on user preferences.
- main: Handles user input and generates a password interactively.
"""


import random  # random number generator
import string


def generate_password(length=20,    # Generates the password
                    use_uppercase=True,
                    use_numbers=True,
                    use_unique=True,
                    longlength=True):
    """
    Generates a random password based on user preferences.

    Args:
        length (int): Length of the password.
        use_uppercase (bool): Include uppercase letters.
        use_numbers (bool): Include numbers.
        use_unique (bool): Include special characters.
        longlength (bool): Allow passwords longer than 20 characters.

    Returns:
        str: The generated password.
    """
    characters = string.ascii_lowercase
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_numbers:
        characters += string.digits
    if use_unique:
        characters += string.punctuation

    if not longlength and length > 20:
        raise ValueError(
            "Password Length cannot be more than 20 characters when you have not Enabled MaxPass")
    if length < 4:
        raise ValueError("Password must be minimum to 4 characters")

    password = ''.join(random.choice(characters) for _ in range(length))
    return password


def ask_yes_no(prompt):
    while True:
        choice = input(prompt).strip().lower()
        if choice in ['y', 'n']:
            return choice == 'y'
        print("Invalid input. Please type 'y' for yes or 'n' for no.")


def main():  # Asks the user questions and feeds the data to the password generator.
    print("Hello, welcome to PyPass!")  # Display the welcome message only once
    while True:  # Loop to restart if an error happens
        try:
            # Ask for longlength / MaxPass
            longlength = ask_yes_no(
                "\nBy default, PyPass restricts passwords to a maximum of 20 characters.\n"
                "If you'd like to enable longer passwords (MaxPass), press 'y'. \n"
                "Otherwise, press 'n'.: "
            )
            if longlength:
                print("MaxPass is Enabled, enjoy!")
            else:
                print("Alrighty, MaxPass is still disabled.")

            # Ask for password length with validation
            while True:
                try:
                    length = int(
                        input("\nWhat length would you like your password to be?: "))
                    if not longlength and length > 20:
                        raise ValueError(
                            "Password cannot be more than 20 characters if MaxPass is not enabled.")
                    if length < 4:
                        raise ValueError(
                            "Password has to be a minimum of 4 characters.")
                    break
                except ValueError as e:
                    print(f"Error: {e}")
            # Ask for preferences
            use_uppercase = ask_yes_no(
                "\nWould you like to include uppercase letters? (y/n): ")
            use_numbers = ask_yes_no(
                "Would you like to include numbers? (y/n): ")
            use_unique = ask_yes_no(
                "Would you like to include special characters (e.g., !@#$%)? (y/n): ")

            # Generate password
            password = generate_password(
                length, use_uppercase, use_numbers, use_unique, longlength)
            print(f"\nYour generated password is: {password}")
            # Ask to generate another
            if not ask_yes_no("\nWould you like to generate another password? (y/n): "):
                print("Thanks for using PyPass! Stay secure 🔐")
            break
        except ValueError as e:
            print(f"Error: {e}")
            print("Let's try that again!\n")


if __name__ == "__main__":
    main()