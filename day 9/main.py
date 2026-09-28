from workouttracker import WorkoutTracker
from datetime import datetime

tracker = WorkoutTracker()

while True:
    print("===== MENU =====")
    print("1. Add Workout")
    print("2. View Workout")
    print("3. Exit")

    choice = input("Option: ")

    if choice == "1":
            while True:
                try:
                    date = input("Date (DD-MM-YYYY): ")
                    datetime.strptime(date, "%d-%m-%Y")
                    break
                except ValueError:
                    print("Invalid Input. Try again.")
            while True:
                    exercise = input("Exercise: ")
                    if exercise == "":
                        print("Fill in the exercise.")
                    else:
                        break
            while True:
                try:
                    sets = int(input("Sets: "))
                    if sets <= 0:
                        print("Number must be greater then 0.")
                    else:
                        break
                except ValueError:
                    print("Invalid Input. Try again.")
            while True:
                try:
                    reps = int(input("Reps: "))
                    if reps <= 0:
                        print("Number must be greater then 0.")
                    else:
                        break
                except ValueError:
                    print("Invalid Input. Try again.")
            while True:
                try:
                    weight = float(input("Weight: "))
                    if weight <= 0:
                        print("Number must be greater then 0.")
                    else:
                        break
                except ValueError:
                    print("Invalid Input. Try again.")

            tracker.add_workout(date, exercise, sets, reps, weight)

    elif choice == "2":
        tracker.view_workout()

    elif choice == "3":
        print("Exiting...")
        break