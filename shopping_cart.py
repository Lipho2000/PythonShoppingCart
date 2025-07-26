# Fixed food items and their prices
menu = {
    "sugar": 48.99,
    "oats": 32.99,
    "steak": 90.95,
    "chicken": 89.95,
    "samp": 55.90,
    "tea": 25.50
}

cart = []  # list to store selected items
total = 0  # variable to track total price

print("🛒 Welcome to the Food Shopping Cart!")
print("Available food items:")
for item, price in menu.items():
    print(f"- {item.title()} : R{price:.2f}")

print("\n📌 Type the name of the product to add it to your cart.")
print("📌 Type 'done' or 'exit' to finish.\n")

while True:
    choice = input("Enter food item: ").strip().lower()

    if choice in ["done", "exit"]:
        break
    elif choice in menu:
        cart.append(choice)
        total += menu[choice]
        print(f"✓ {choice.title()} added. Current Total: R{total:.2f}")
    else:
        print("⚠️ That item is not on the list. Please choose from the available items.")

# Final output
print("\n🛍️ Your Cart:")
if cart:
    for item in cart:
        print(f"- {item.title()} : R{menu[item]:.2f}")
    print(f"\n💵 Total Cost: R{total:.2f}")
else:
    print("Your cart is empty.")
