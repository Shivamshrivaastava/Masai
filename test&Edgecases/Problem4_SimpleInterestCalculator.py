def calculate_simple_interest(principal, rate, time):
    # Calculate simple interest using the formula
    simple_interest = (principal * rate * time) / 100
    return simple_interest

def main():
    try:
        # Prompt the user to enter principal, rate, and time
        principal = float(input("Enter the principal amount: $"))
        rate = float(input("Enter the annual interest rate (%): "))
        time = float(input("Enter the time period (in years): "))
        
        # Calculate the simple interest using the calculate_simple_interest function
        interest = calculate_simple_interest(principal, rate, time)
        
        # Print the simple interest
        print(f"The simple interest is: ${interest:.2f}")
    except ValueError:
        print("Invalid input. Please enter numeric values.")

if __name__ == "__main__":
    main()
