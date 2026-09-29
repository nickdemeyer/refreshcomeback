from workouttracker import WorkoutTracker
from mealtracker import MealTracker
from datetime import datetime

tracker = WorkoutTracker()
meal_tracker = MealTracker()

while True:
    print("==== MENU ====")
    print("1. WORKOUTS")
    print("2. MEALS")
    print("3. EXIT")

    keuze = input("Select to continue: ")

    if keuze == "1":
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
                    print("EXIT")
                    break 

    elif keuze == "2":
        while True:
            print("==== MENU ====")
            print("1. Add Meal")
            print("2. View Meal")
            print("3. Exit")

            choice = input("Choose option: ")

            if choice == "1":
                while True:
                    try:
                        date = input("Date (DD-MM-YYYY): ")
                        datetime.strptime(date, "%d-%m-%Y")
                        break
                    except ValueError:
                        print("Invalid Input. Try again.")
                while True:
                    name = input("Meal: ")
                    if name == "":
                        print("Fill in the Meal.")
                    else:
                        break
                while True:
                    try:
                        calories = int(input("Calories: "))
                        if calories <= 0:
                            print("Input must be greater then 0.")
                        else:
                            break
                    except ValueError:
                        print("Invalid Input.")
                while True:
                    try:
                        protein = int(input("Protein: "))
                        if protein <= 0:
                            print("Input must be greater then 0.")
                        else:
                            break
                    except ValueError:
                        print("Invalid Input.")
                while True:
                    try:
                        carbs = int(input("Carbs: "))
                        if carbs <= 0:
                            print("Input must be greater then 0.")
                        else:
                            break
                    except ValueError:
                        print("Invalid Input.")
                while True:
                    try:
                        fats = int(input("Fats: "))
                        if fats <= 0:
                            print("Input must be greater then 0.")
                        else:
                            break
                    except ValueError:
                        print("Invalid Input.")
                meal_tracker.add_meal(date, name, calories, protein, carbs, fats)

            elif choice == "2":
                meal_tracker.view_meal()

            elif choice == "3":
                print("EXIT")
                break

    elif keuze == "3":
        print("Closing Application....")
        break