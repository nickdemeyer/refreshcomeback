input_weight = int(input("Your weight: "))
input_height = float(input("Your height: "))
bmi = input_weight / (input_height * input_height)

if bmi < 18.5:
    print("underweighted")
elif bmi < 25:
    print("healthy weight")
elif bmi < 30:
    print("overweighted")
elif bmi >= 30:
    print("obese")