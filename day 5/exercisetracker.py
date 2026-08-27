workouts = []

def add_exercise(exercise):
    name_input = input("exercise: ")
    set_input = input("sets: ")
    rep_input = input("reps: ")

    workout = {"exercise": name_input,
               "sets": set_input,
               "reps": rep_input}

    exercise.append(workout)
    print("workout added")

def view_workouts(exercise):
    for i in exercise:
        print(f"{i["exercise"]}: {i["sets"]} sets x {i["reps"]} reps")

while True:
    print("=== MENU WORKOUTS ===")
    print("1. View Workouts")
    print("2. Add Workouts")
    print("3. Exit")

    choice = input("choose to continue: ")

    if choice == "1":
        view_workouts(workouts)
    elif choice == "2":
        add_exercise(workouts)
    else:
        print("exiting...")
        break