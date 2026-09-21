import json

with open("day 6/workouts.json", "r") as bestand:
    loaded_workouts = json.load(bestand)

for workout in loaded_workouts:
    print(workout)