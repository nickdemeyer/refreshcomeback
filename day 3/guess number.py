number = 7

while True:
    user_input = int(input("guess number: "))
    if user_input == number:
        print("You Guessed it!")
        break
    else:
        print("Try Again!")
        