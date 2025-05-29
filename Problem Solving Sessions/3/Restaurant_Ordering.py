# Restaurant Ordering System

# Menu items (item_number: (name, price))
menu = {
    1: ("Garlic Bread", 3.50),
    2: ("Chicken Wings", 5.00),
    3: ("Spaghetti Bolognese", 10.00),
    4: ("Grilled Chicken with Veggies", 12.50),
    5: ("Soda", 2.00),
    6: ("Fresh Juice", 3.00),
    7: ("Chocolate Cake", 4.00),
    8: ("Ice Cream Sundae", 3.50)
}

order = {}  # Stores item_number: (name, price, quantity)

def display_menu():
    print("\n🧾 Welcome to Foodie's Delight!")
    print("Please choose from our delicious menu:\n")

    print("🍽️ Appetizers:")
    print("1. Garlic Bread - $3.50")
    print("2. Chicken Wings - $5.00")

    print("\n🍝 Main Course:")
    print("3. Spaghetti Bolognese - $10.00")
    print("4. Grilled Chicken with Veggies - $12.50")

    print("\n🥤 Drinks:")
    print("5. Soda - $2.00")
    print("6. Fresh Juice - $3.00")

    print("\n🍰 Desserts:")
    print("7. Chocolate Cake - $4.00")
    print("8. Ice Cream Sundae - $3.50")

    print("\n👉 Enter item number to add to your order.")
    print("✅ Type 'done' when finished.\n")

def take_order():
    while True:
        user_input = input("Enter item number (or 'done'): ")
        if user_input.lower() == 'done':
            break
        if not user_input.isdigit():
            print("⚠️ Please enter a valid number.")
            continue
        item_number = int(user_input)
        if item_number in menu:
            qty = input(f"Enter quantity for {menu[item_number][0]}: ")
            if qty.isdigit():
                qty = int(qty)
                if item_number in order:
                    order[item_number] = (
                        menu[item_number][0],
                        menu[item_number][1],
                        order[item_number][2] + qty
                    )
                else:
                    order[item_number] = (
                        menu[item_number][0],
                        menu[item_number][1],
                        qty
                    )
                print(f"✅ Added {qty} x {menu[item_number][0]} to your order.\n")
            else:
                print("⚠️ Invalid quantity. Try again.")
        else:
            print("❌ Invalid item number. Try again.")

def print_final_bill():
    print("\n🧾 Your Final Bill:")
    total = 0
    for item_number, (name, price, qty) in order.items():
        item_total = price * qty
        total += item_total
        print(f"- {name} x{qty} @ ${price:.2f} each = ${item_total:.2f}")

    tax = total * 0.08  # 8% tax
    grand_total = total + tax
    print(f"\nSubtotal: ${total:.2f}")
    print(f"Tax (8%): ${tax:.2f}")
    print(f"Total Due: ${grand_total:.2f}")
    print("\n🍽️ Thank you for dining with us! Have a great day!\n")

# Main Program
def main():
    display_menu()
    take_order()
    if order:
        print_final_bill()
    else:
        print("🛑 No items ordered. Come back soon!")

# Run the program
main()
# This code implements a simple restaurant ordering system where users can select items from a menu,
# specify quantities, and receive a final bill with tax included. It uses a dictionary to manage the menu