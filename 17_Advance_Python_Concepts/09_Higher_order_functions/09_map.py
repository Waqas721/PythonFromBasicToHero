numbers=[1,2,3,45,4,21]
def square(x):
    return x*x

new=list(map(square,numbers))
print(new)

# num=[1,2,3,4,5]
# newlist=list(map(lambda x:x*x,num))
# print(newlist)