#BMI calculator

input_weight = int(input("Your weight: "))
input_height = float(input("Your height: "))
bmi = input_weight / (input_height * input_height)

print("calculating bmi...")
print(f"Your BMI is {bmi}")