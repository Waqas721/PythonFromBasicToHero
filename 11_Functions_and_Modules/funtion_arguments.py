def add(a,b):  #a,b are parameter
    x=a+b
    return x

def add1(a,b,c=0):
     x=a+b
     return x+c
    
def greet(name="Guest"):
    return f"Hello, {name}!"

def student(name, age):
    print(f"Name: {name}, Age: {age}")
 




c=add(3,5) #3 and 5 are arguments
print(c)

d=add1(3,5,3) 
print(d)

print(greet()) # Output: Hello, Guest!
print(greet("Waqas")) # Output: Hello, Waqas!


e=add(b=9,a=4) 
print(e)
student(age=20, name="Bob")