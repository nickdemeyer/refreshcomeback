exercises = []

def add_exercise(exercise):
    user_input = input("add exercise: ")
    exercise.append(user_input)
    print("exercise added")
    

def view_exercises(exercise):
    for l in exercise:
        print(f"{l}")


while True:
    print("==== MENU ====")
    print("1. View Exercises")
    print("2. Add Exercise")
    print("3. Finish")

    choice = input("choose to continue: ")

    if choice == "1":
        view_exercises(exercises)
    elif choice == "2":
        add_exercise(exercises)
    else:
        break