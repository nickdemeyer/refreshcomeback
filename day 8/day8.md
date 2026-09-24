basis herhaling try/except en value error

workouttracker dag 7 aanpassingen doen:
- Convert sets, reps, weight to actual numbers (int/float) instead of leaving them as strings — fix that now
- Add validation so the program can't crash: if the user types a letter where a number is expected, catch it and ask again instead of crashing
- Add a check so sets/reps/weight can't be negative or zero
- Test it by deliberately trying to break it — type letters, negative numbers, empty input