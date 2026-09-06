recepts = []

#keys used: receptname - preperationtime - ingredients
def add_recepts(recept):
    user_input1 = input("name recept: ")
    user_input2 = input("preperation time: ")
    user_input3 = input("ingredients: ")
    r = {"receptname": user_input1, "preperationtime": user_input2, "ingredients": user_input3}
    recept.append(r)
    print("recept added")
    
def view_recepts(recept):
    for r in recept:
        print("=============================================================")
        print(f"recept: {r["receptname"]}")
        print(f"prep time: {r["preperationtime"]} ")
        print(f"ingredients: {r["ingredients"]}")
        print("=============================================================")

def search_recept(recept):
    user_input = input("search: ")
    for r in recept:
        if r["receptname"] == user_input:
            print("==================================")
            print(f"{r}")
            print("==================================")

while True:
    print("=== RECEPT BOOK MENU ===")
    print("1. View Recepts")
    print("2. Add Recepts")
    print("3. Search Recept")
    print("4. Close App")

    choice = input("Choose: ")

    if choice == "1":
        view_recepts(recepts)
    elif choice == "2":
        add_recepts(recepts)
    elif choice == "3":
        search_recept(recepts)
    elif choice == "4":
        print("exiting...")
        break