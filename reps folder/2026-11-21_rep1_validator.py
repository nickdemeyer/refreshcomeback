#validatie van een rep waarbij getal een volledige getal is en geen komma of 0 kan zijn getal moet groter dan 0 zijn want je hebt altijd sws 1 rep

#functie maken
#if statement gebruiken met de validatie
#print tekst als het niet klopt 
#anders return None dat alles goed is

def check_whole_number(value):
    if value is not int or value <= 0:
        print("number must be whole and above 0.")
    return None


#vergeten van type() te gebruiken bij:
# if type(value) is not int -> de reden dat we type gebruiken is voor integer/float/str....
#ik had return moeten doen ipv print, print toont alleen de tekst in terminal en return de value is whatever in die value gestoken word waar de fucntie aangeroepen is.