def fact(n):
    if n==1 or n==0:
        return 1
    else:
        return n*fact(n-1)
    
# a=fact(3)
# print(a)
    
'''
0 1 1 2 3 5 8 13..

fib(0)=0
fib(1)=1
fib(2)=fib(0)+fib(1)
fib(3)=fib(1)+fib(2)
fib(4)=fib(2)+fib(3)
fib(n)=fib(n-2)+fib(n-1)
'''
def fib(n):
    if (n==0 or n==1):
      return n
    else: 
        return fib(n-2)+fib(n-1)

for i in range(8):
    print(fib(i),end="," if i<7 else " ")
    



