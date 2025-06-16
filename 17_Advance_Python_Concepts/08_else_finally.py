'''
try:
    a=345/10
except Exception as e:
    print(e)
# Gets executed when there is no error in the try block
else:
    print("Hey I am good")
'''


def divide(a,b):
    try:
        c=a/b
        print(c)
        return c
        
    except Exception as e:
        print(e)
        return None

    # This is always executed no matter if try completely executes or not
    finally:
        print("This is always executed")
    #print("This is always executed")  # this will not execute if error is occured but incase of not a funtion it will execute
        
a=int(input("Enter first number:"))
b=int(input("Enter second number:"))
divide(a,b)