from functools import reduce
# def sum(a,b):
#     return a+b

def sum(*args):
    # args willl be a tple of all the values passed to sum
    #print(args) # return a tuple
    total=0
    # a=(reduce(lambda x,y:x+y,args))
    # print(a)
    for item in args:
        total+=item
    return total
    

#print(sum(2,3,34)) # will throw an error 
print(sum(342,2,7,9))