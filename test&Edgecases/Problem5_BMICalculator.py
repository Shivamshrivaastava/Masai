def calculate_bmi(weight, height):
    # Calculate BMI using the formula: weight / (height^2)
    bmi = weight / (height ** 2)
    return bmi

def main():
    try:
        # Prompt the user to enter weight in kilograms and height in meters
        weight = float(input("Enter your weight in kilograms: "))
        height = float(input("Enter your height in meters: "))
        
        # Calculate BMI using the calculate_bmi function
        bmi = calculate_bmi(weight, height)
        
        # Print the calculated BMI
        print(f"Your Body Mass Index (BMI) is: {bmi:.2f}")
    except ValueError:
        print("Invalid input. Please enter numeric values.")

if __name__ == "__main__":
    main()
