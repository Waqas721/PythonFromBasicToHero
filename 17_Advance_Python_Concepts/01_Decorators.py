#Decorator is a function that takes a function, it creates a new function inside it's body ( wrapper) then it returns that new function

def decorator(func):
    def wrapper():
        print("I am about to execute a function...")
        func()
        print("U have executed this function...")
    return wrapper

@decorator
def sayHello():
    print("Hello !")
    

sayHello()

# f=decorator(sayHello)
# f()

'''
f will look something like this
def f():
    print("I am about to execute a function...")
    print("Hello !")
    print("U have executed this function...")

'''