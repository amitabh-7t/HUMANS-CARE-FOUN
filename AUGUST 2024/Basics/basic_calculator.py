def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):

    if y == 0:
        return "Error! Division by zero."
    else:        
        return x / y
    
def power(x, y):
    return x ** y

def main():
    print("Welcome to the Basic Calculator!")
    print("Select operation:")
    print(" + for Add")
    print(" - for Subtract")
    print(" * for Multiply")
    print(" / for Divide")
    print(" ** for Power")

    while True:
        choice = input("Enter your choice ( + , - , * , / , ** ): ")

        if choice in ( "+" ,"-" , "*" , "/" ,"**"):
            try:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
            except ValueError:
                print("Invalid input! Please enter numerical values.")
                continue

            if choice == '+':
                print(f"{num1} + {num2} = {add(num1, num2)}")

            elif choice == '-':
                print(f"{num1} - {num2} = {subtract(num1, num2)}")

            elif choice == '*':
                print(f"{num1} * {num2} = {multiply(num1, num2)}")

            elif choice == '/':
                print(f"{num1} / {num2} = {divide(num1, num2)}")
            
            elif choice == '**':
                print(f"{num1} ^ {num2} = {power(num1, num2)}")

            next_calculation = input("Do you want to perform another calculation? (Y/N): ")
            if next_calculation.lower() != 'y':
                break
        else:
            print("Invalid Input! Please choose a valid operation.")

    print("Thank you for using the Basic Calculator!")

if __name__ == "__main__":
    main()