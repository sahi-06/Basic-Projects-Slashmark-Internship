import random

def display_menu():
    print("\nNumber Guessing Game")
    print("1. Start New Game")
    print("2. Exit")

def start_game():
    number_to_guess = random.randint(1, 100)
    attempts = 0
    print("I have selected a number between 1 and 100. Can you guess it?")
    
    while True:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1
            
            if guess < number_to_guess:
                print("Too low! Try again.")
            elif guess > number_to_guess:
                print("Too high! Try again.")
            else:
                print(f"Congratulations! You guessed the number in {attempts} attempts.")
                break
        except ValueError:
            print("Please enter a valid number.")

def main():
    while True:
        display_menu()
        choice = input("Choose an option (1-2): ")
        
        if choice == '1':
            start_game()
        elif choice == '2':
            print("Exiting the game. Goodbye!")
            break
        else:
            print("Invalid choice. Please choose 1 or 2.")

if __name__ == "__main__":
    main()
