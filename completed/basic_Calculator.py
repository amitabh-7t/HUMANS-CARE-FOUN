# calculator -> 1. addition 2. subtraction 3.multiplication 4. division 5. nth power 6. nth root   9.modulus 7. exit

def addition(value1 , value2):
    return value1 + value2

def subtraction(value1 , value2):
    return value1 - value2

def multiplication(value1 , value2):
    return value1 * value2

def division(value1 , value2):
    if (value2 != 0) :
        return (value1 / value2)
    else:
        return "division by zero is not possible"

def nth_power(value1 , value2 ):
    return (value1) ** (value2)

def nth_root(value1 , value2 ):
    return value1 ** (1 / value2)

def modulus(value1):
    return abs(value1)

def tata_bye_bye(): #quit the program
    print("fir milenge...")
    return False

def calculator():
    while True:
        print("\nCalculator MENU : ")
        print("1.Addition")
        print("2.Substraction")
        print("3.Multiplication")
        print("4.Division")
        print("5.Nth power")
        print("6.Nth root")
        print("7.Modulus")
        print("8.Exit")


        choice =  input("Enter the option: (1/2/3/4/5/6/7/8) ") # choice:str = input("enter value")
        if (choice in ["1","2","3","4","5","6","7"]):
            value1=float(input("Enter the first value: "))
            value2=float(input("Enter the second value: "))

            if choice == "1":
                print(f"Result: {addition(value1, value2)}")

            elif choice == "2":
                print(f"Result: {subtraction(value1, value2)}")

            elif choice == "3":
                print(f"Result: {multiplication(value1, value2)}")
            
            elif choice == "4":
                print(f"Result: {division(value1, value2)}")

            elif choice == "5":
                print(f"Result: {nth_power(value1, value2)}")

            elif choice == "6":
                print(f"Result: {nth_root(value1, value2)}")

            elif choice == "7":
                print(f"Result: {modulus(value1)}")

        elif choice =="8":
            if tata_bye_bye() == False:
                break

        else:
            print("sahab galti ho gyi ")
        
calculator()

        








