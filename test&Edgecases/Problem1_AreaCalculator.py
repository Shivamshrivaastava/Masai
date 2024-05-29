def calculate_area(base, height):
    # Check if either base or height is negative
    if base < 0 or height < 0:
        return "Invalid input, base and height must be positive numbers."
    # Calculate the area using the formula (Base * Height) / 2
    area = (base * height) / 2
    return area

def main():
    try:
        # Prompt user to enter the base and height of the triangle
        base = float(input("Enter the base of the triangle: "))
        height = float(input("Enter the height of the triangle: "))
        # Calculate the area using the calculate_area function
        result = calculate_area(base, height)
        # Print the result
        if isinstance(result, str):  # Check if result is a string (error message)
            print(result)
        else:
            print(f"The area of the triangle is: {result}")  # Print the calculated area
    except ValueError:
        print("Invalid input, please enter numeric values.")  # Handle non-numeric inputs

if __name__ == "__main__":
    main()
