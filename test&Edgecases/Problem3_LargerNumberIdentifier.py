def compare_numbers(num1, num2):
    # Compare num1 and num2
    if num1 > num2:
        return f"{num1} is larger than {num2}"
    elif num1 < num2:
        return f"{num2} is larger than {num1}"
    else:
        return f"{num1} and {num2} are equal"

def main():
    try:
        # Prompt the user to enter two numbers
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        # Call the compare_numbers function to determine the comparison result
        comparison_result = compare_numbers(num1, num2)
        # Print the comparison result
        print(comparison_result)
    except ValueError:
        print("Invalid input. Please enter numeric values.")

if __name__ == "__main__":
    main()
