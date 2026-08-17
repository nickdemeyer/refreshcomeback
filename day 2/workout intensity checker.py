user_input = int(input("What is your heartrate? "))

if user_input <= 60:
    print("Low heartrate intensity")
elif user_input <= 119:
    print("Moderate heartrate intensity")
elif user_input >= 120:
    print("High heartrate intensity")