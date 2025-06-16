def sum(a,b):
    #a and b are local varaiables
    c=a+b
    z=1 # it create a local variable called z which is detroyed after this function returns
    return c

def greet():
    z =32 # local variable
    print("Hello")

z=8  # Z is a gloabl variable
print(z)
print(sum(4,6))
print(z)
