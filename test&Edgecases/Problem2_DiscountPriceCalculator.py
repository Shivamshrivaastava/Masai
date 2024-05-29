def calculate_final_price(price):
    # Check if the price is more than $20
    if price > 20:
        # Calculate the discount amount (10% of the price)
        discount = 0.1 * price
        # Calculate the final price after applying the discount
        final_price = price - discount
        return final_price
    else:
        # If the price is $20 or less, no discount is applied
        return price

def main():
    try:
        # Prompt the user to enter the price of the item
        price = float(input("Enter the price of the item: $"))
        # Calculate the final price using the calculate_final_price function
        final_price = calculate_final_price(price)
        # Print the final price
        print(f"The final price after discount is: ${final_price:.2f}")
    except ValueError:
        print("Invalid input. Please enter a numeric value for the price.")

if __name__ == "__main__":
    main()
