user_input = int(input("Fill in your test score: "))

if user_input >= 90:
    print("Grade: A")
elif user_input >= 80:
    print("Grade: B")
elif user_input >= 70:
    print("Grade: C")
elif user_input >= 60:
    print("Grade: D")
else: 
    print("Grade: F")