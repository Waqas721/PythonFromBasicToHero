try:
    a=int(input("Enter the first number:"))
    b=int(input("Enter the second number:"))
    
    print("What kind of operation do you want to perform Press + for addition\nPress - for subraction\nPress / for division\nPress * for multiplication")
    o=input("Enter operation:")
    match o:
        case '+':
            print(f"The result is : {a+b}")
        case '-':
            print(f"The result is : {a-b}")
        case '/':
            print(f"The result is : {a/b}")
        case '*':
            print(f"The result is : {a*b}")
        case default:
            print("Some error occured")
except Exception as e:
    print("Enter a valid value of a and b")

