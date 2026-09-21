import json

workout = {"date": "21/08/26",
           "exercise": "pullup",
           "reps": 10,
           "sets": 4}

with open("workout.json", "w") as bestand:
    json.dump(workout, bestand)