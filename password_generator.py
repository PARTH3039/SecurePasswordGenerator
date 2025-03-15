import random
import string

# Function to validate user input
def get_user_input(prompt, min_value, max_value):
    while True:
        try:
            value = int(input(prompt))
            if value < min_value or value > max_value:
                print(f"Please enter a value between {min_value} and {max_value}.")
            else:
                return value
        except ValueError:
            print("Invalid input. Please enter a number.")

# Function to generate the password
def generate_password(length, num_letters, num_digits, num_specials):
    if num_letters + num_digits + num_specials > length:
        print("Error: The sum of letters, digits, and special characters exceeds the total length.")
        return None
    
    # Generate required characters
    letters = random.choices(string.ascii_letters, k=num_letters)
    digits = random.choices(string.digits, k=num_digits)
    specials = random.choices(string.punctuation, k=num_specials)
    
    # Fill remaining characters if needed
    remaining_length = length - (num_letters + num_digits + num_specials)
    all_characters = letters + digits + specials
    all_characters += random.choices(string.ascii_letters + string.digits + string.punctuation, k=remaining_length)

    # Shuffle and return password
    random.shuffle(all_characters)
    password = ''.join(all_characters)
    return password

# Main function
def main():
    print("--- Secure Password Generator ---\n")

    # Step 1: Get user inputs
    length = get_user_input("Enter total password length (min 8): ", 8, 100)
    num_letters = get_user_input("Enter number of letters: ", 0, length)
    num_digits = get_user_input("Enter number of digits: ", 0, length)
    num_specials = get_user_input("Enter number of special characters: ", 0, length)

    # Step 2: Validate inputs
    if num_letters + num_digits + num_specials > length:
        print("Error: The sum of letters, digits, and special characters exceeds the total length.")
        return

    # Step 3: Generate password
    password = generate_password(length, num_letters, num_digits, num_specials)
    if password:
        print(f"Generated password: {password}")

    # Step 4: Save password to file
    with open("generated_password.txt", "w") as file:
        file.write(password)
        print("Password saved to generated_password.txt")

if __name__ == "__main__":
    main()
