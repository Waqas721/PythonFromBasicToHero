# while True:
#     try:
#         a=int(input("Enter first number:"))
#         b=int(input("Enter second number:"))
#         print(f"The divison is {a/b}")
        
#     except ValueError:
#         print("Please donot perform bad typecast")
        
#     except ZeroDivisionError:
#         print("Hey donot divide by 0")
        
#     except Exception as e:
#         print("Some error occured",e)

a=int(input("Enter first number:"))
b=int(input("Enter second number:"))
if b==0:
    raise ValueError("Please donot divide by Zero")
print(f"The divison is {a/b}")

