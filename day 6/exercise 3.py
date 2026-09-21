import json

workouts = [{"exercise": "pulldown", "sets": 4, "reps": 10}, 
            {"exercise": "chestpress", "sets": 4, "reps": 12},
            {"exercise": "squat", "sets": 4, "reps": 8}]

with open("workouts.json", "w") as bestand:
    json.dump(workouts, bestand)