import json

with open("day 6/workout.json", "r") as bestand:
    workout_data = json.load(bestand)

print(workout_data)