balance = 1000  # Initial balance
PIN = "1234"  # Correct PIN

def authenticate_user(pin_input):
    return pin_input == PIN

def update_balance(amount, transaction_type):
    global balance
    if transaction_type == "withdraw" and amount > balance:
        print("Insufficient funds.")
    else:
        balance += amount if transaction_type == "deposit" else -amount
        print(f"${amount} {transaction_type}ed successfully.")

def transaction_menu():
    print("\nATM Services Menu:")
    print("1. Display Balance")
    print("2. Withdraw Money")
    print("3. Deposit Money")
    print("4. Exit")

def main():
    print("Welcome to the ATM!")
    if not authenticate_user(input("Enter your 4-digit PIN: ")):
        print("Authentication failed.")
        return

    while True:
        transaction_menu()
        choice = input("Choose an option (1-4): ")

        if choice == "1":
            print(f"Your current balance is: ${balance}")
        elif choice in {"2", "3"}:
            amt = float(input("Enter amount: "))
            update_balance(amt, "withdraw" if choice == "2" else "deposit")
        elif choice == "4":
            print("Thank you for using the ATM. Goodbye!")
            break
        else:
            print("Invalid option. Try again.")

# Start the program
main()
