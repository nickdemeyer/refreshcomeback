exercises = []

for exercise in range(5):
    user_input = input("give exercise name: ")
    exercises.append(user_input)

for i, exercise in enumerate(exercises, start=1):
    print(i, exercise)