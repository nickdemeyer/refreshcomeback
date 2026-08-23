getallen = [5,10,5,10,3]
lijst = [3, 6, 7]
def sum_numbers(getal):
    totaal = 0
    for g in getal:
        totaal = g + totaal
    return totaal

uitkomst = sum_numbers(getallen)
print(uitkomst)

uitkomst2 = sum_numbers(lijst)
print(uitkomst2)