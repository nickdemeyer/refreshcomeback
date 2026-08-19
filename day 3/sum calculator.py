getallen = []

while True:
    user_input = int(input("give 5 numbers one by one: "))
    getallen.append(user_input)
    if len(getallen) == 5:
        break
totaal = 0

for getal in getallen:
    totaal = totaal + getal

print(f"the sum is {totaal}")