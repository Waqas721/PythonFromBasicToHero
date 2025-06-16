def repeat(n):
    def decorator(func):
        def wrapper(a):  # a is parameter
            for i in range(n): # n is how many times i want to repeat the function
                    func(a)   # a is argument
        return wrapper
    return decorator
    
@repeat(3)
def say_hello(a):
    print(f"Hello, {a}!")
    
'''
It replaces the function say_hello with this
def decorator(func):
    def wrapper(a):  # a is parameter
        for i in range(n): # n is how many times i want to repeat the function
            say_hello(a)       # a is argument
        return wrapper
'''

say_hello("Waqas")
