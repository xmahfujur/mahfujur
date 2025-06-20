import math

def sifi_calculator():
    print("Welcome to the Sci-Fi Calculator!")
    print("Select operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Power (x^y)")
    print("6. Square Root (√x)")
    print("7. Sine (sin x)")
    print("8. Cosine (cos x)")
    print("9. Tangent (tan x)")
    print("0. Exit")

    while True:
        choice = input("Enter choice (0-9): ")
        if choice == '0':
            print("Exiting Sci-Fi Calculator. Goodbye!")
            break

        if choice in ['1', '2', '3', '4', '5']:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            if choice == '1':
                print(f"Result: {num1 + num2}")
            elif choice == '2':
                print(f"Result: {num1 - num2}")
            elif choice == '3':
                print(f"Result: {num1 * num2}")
            elif choice == '4':
                if num2 == 0:
                    print("Error: Division by zero!")
                else:
                    print(f"Result: {num1 / num2}")
            elif choice == '5':
                print(f"Result: {math.pow(num1, num2)}")

        elif choice == '6':
            num = float(input("Enter number: "))
            if num < 0:
                print("Error: Cannot take square root of negative number!")
            else:
                print(f"Result: {math.sqrt(num)}")

        elif choice in ['7', '8', '9']:
            angle = float(input("Enter angle in degrees: "))
            radians = math.radians(angle)
            if choice == '7':
                print(f"Result: {math.sin(radians)}")
            elif choice == '8':
                print(f"Result: {math.cos(radians)}")
            elif choice == '9':
                print(f"Resuldt: {math.tan(radians)}")
        else:
            print("Invalid input. Please try again.")

if __name__ == "__main__":
    sifi_calculator()
# This code is a simple Sci-Fi Calculator that performs various mathematical operations.
# It includes addition, subtraction, multiplication, division, power, square root,  