temp = input("Enter value of temperature with unit (C, F, K): ")
convert = input("Enter which unit to convert to (C, F, K): ").lower()
value = float(temp[:-1])
from_unit = temp[-1].lower()

if from_unit == 'c':
    if convert == 'f':
        new_temp = (value * 9/5) + 32
        print(f"The converted temperature is {new_temp:.2f} F")
    elif convert == 'k':
        new_temp = value + 273.15
        print(f"The converted temperature is {new_temp:.2f} K")
elif from_unit == 'f':
    if convert == 'c':
        new_temp = (value - 32) * 5/9
        print(f"The converted temperature is {new_temp:.2f} C")
    elif convert == 'k':
        new_temp = (value - 32) * 5/9 + 273.15
        print(f"The converted temperature is {new_temp:.2f} K")
elif from_unit == 'k':
    if convert == 'c':
        new_temp = value - 273.15
        print(f"The converted temperature is {new_temp:.2f} C")
    elif convert == 'f':
        new_temp = (value - 273.15) * 9/5 + 32
        print(f"The converted temperature is {new_temp:.2f} F")
else:
    print("Invalid unit entered.")
