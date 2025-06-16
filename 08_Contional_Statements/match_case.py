a=int(input("Enter a number between 1 and 10.."))
match(a):
    case 1:
        print("You won a charger")
    case 4:
         print("You won a camera")
    case 6:
         print("You won a $3")
    case _: #default
        print("Better luck next time")