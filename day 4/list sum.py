getallen = [5,10,5,10,3]

def sum_numbers(getal):
    totaal = 0
    for g in getal:
        totaal = g + totaal
    return totaal

uitkomst = sum_numbers(getallen)
print(uitkomst)