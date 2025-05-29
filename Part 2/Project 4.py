
def generate_bill(*items):
    print("\n🧾🛍️ Welcome to Python Supermarket 🛍️🧾")
    print("-"*40)
    print(f"{'Item':<20}{'Price (₹)':>15}")
    total = 0
    for item in items:
        name,price = item
        print(f"{name:<20}{price:>15.2f}")
        total += price
    
    gst = total * 0.05 # 5% GST
    final_amount = total + gst

    print("-"*40)
    print(f"{'subtotal':<20}{total:>15.2f}")
    print(f"{'GST (5%)':<20}{gst:>15.2f}")
    print(f"{'Total Amount':<20}{final_amount:>15.2f}")
    print("-"*40)
    print("🙏 Thank you for shoppint with us! 🙏\n")

def main():
    items = []
    while True:
        name = input("Enter item name (or 'done' to finish):").strip()
        if name == "done":
            break
        try:
            price = int(input(f"Enter price for '{name}': ₹"))
            items.append((name,price))
        except ValueError:
            print("❌ Invalid price. Please enter a number")
    if items:
        generate_bill(*items)
    else:
        print("🛒 No items added. Exiting...")

main()



