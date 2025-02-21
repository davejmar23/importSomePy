import random
import joke
import advice

def main():
    """Main function to display a random joke or piece of advice."""
    print("Welcome! Do you want to hear a joke or get some advice?")
    choice = input("Type 'joke' for a joke or 'advice' for advice: ").strip().lower()
    
    if choice == 'joke':
        print("\nHere's a joke for you:")
        print(random.choice(joke.joke_list))
    elif choice == 'advice':
        print("\nHere's some advice:")
        print(random.choice(advice.advice_list))
    else:
        print("\nInvalid choice. Please run the program again and type 'joke' or 'advice'.")

if __name__ == "__main__":
    main()
