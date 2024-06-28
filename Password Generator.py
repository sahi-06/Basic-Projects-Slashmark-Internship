import random
import string

def display_menu():
    print("\nPassword Generator")
    print("1. Generate a password")
    print("2. Exit")

def generate_password(length, use_uppercase, use_lowercase, use_digits, use_special):
    character_pool = ''
    
    if use_uppercase:
        character_pool += string.ascii_uppercase
    if use_lowercase:
        character_pool += string.ascii_lowercase
    if use_digits:
        character_pool += string.digits
    if use_special:
        character_pool += string.punctuation
    
    if not character_pool:
        print("No character types selected. Please select at least one character type.")
        return None
    
    password = ''.join(random.choice(character_pool) for _ in range(length))
    return password

def main():
    while True:
        display_menu()
        choice = input("Choose an option (1-2): ")
        
        if choice == '1':
            try:
                length = int(input("Enter the length of the password: "))
                if length <= 0:
                    print("Length should be a positive integer.")
                    continue
            except ValueError:
                print("Please enter a valid number for the length.")
                continue

            use_uppercase = input("Include uppercase letters? (y/n): ").lower() == 'y'
            use_lowercase = input("Include lowercase letters? (y/n): ").lower() == 'y'
            use_digits = input("Include digits? (y/n): ").lower() == 'y'
            use_special = input("Include special characters? (y/n): ").lower() == 'y'
            
            password = generate_password(length, use_uppercase, use_lowercase, use_digits, use_special)
            if password:
                print(f"Generated password: {password}")
        elif choice == '2':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please choose 1 or 2.")

if __name__ == "__main__":
    main()
