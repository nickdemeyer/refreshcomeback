recepts = []

#keys used: receptname - preperationtime - ingredients
def add_recepts(recept):
    user_input1 = input("name recept: ")
    user_input2 = input("preperation time: ")
    user_input3 = input("ingredients: ")
    r = {"receptname": user_input1, "preperationtime": user_input2, "ingredients": user_input3}
    recept.append(r)
    print("recept added")
    
    
while True:
    print("=== RECEPT BOOK MENU ===")
    print("1. View Recepts")
    print("2. Add Recepts")
    print("3. Search Recept")
    print("4. Close App")

    choice = input("Choose: ")

    if choice == "2":
        add_recepts(recepts)
    else:
        print("exiting...")
        break