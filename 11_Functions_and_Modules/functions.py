# a=4
# b=2
# c=1

# average=(a+b+c)/3
# print(average)

# a1=6
# b1=7
# c1=12

# average1=(a1+b1+c1)/3
# print(average1)

def average(a,b,c):
    d=(a+b+c)/3.0
    print(d)


def average1(a,b,c):
    d=(a+b+c)/3.0
    return d

def greet(name):
 return f"Hello, {name}!"

print(greet("Alice"))
average(3,5,1)

o1=average(4,2,1)
print(o1)    #None

o2=average1(4,2,1)
print(o2)  