num1 = float(input("first number: "))
num2 = float(input("second number: "))

def add_calculator(num1, num2):
    return num1 + num2

def substract_calculator(num1, num2):
    return num1 - num2

def multiply_calculator(num1, num2):
    return num1 * num2

def divide_calculator(num1, num2):
    return num1 / num2

uitkomst = add_calculator(num1, num2)
print(uitkomst)

uitkomst2 = substract_calculator(num1, num2)
print(uitkomst2)

uitkomst3 = multiply_calculator(num1, num2)
print(uitkomst3)

uitkomst4 = divide_calculator(num1, num2)
print(uitkomst4)