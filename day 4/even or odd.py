number = int(input("give number: "))

def control(number):
    number = number % 2
    return "even" if number == 0 else "odd"

uitkomst = control(number)

print(uitkomst)