class Employee:
    company="HP"
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
        
    def __str__(self):
        return f"The name is {self.name} and the salary is {self.salary}"
    
    def __repr__(self):
        return f"name:{self.name}\nsalary:{self.salary}"
    
    #from operator overloading
    # def __add__(self,p):
    #      return Point((self.x+p.x),(self.y+p.y))
    
    def __len__(self):
        return len(self.name)
         
e=Employee("Harry",43566)
# The code snippet `print(e.name, e.salary)` is printing the name and salary attributes of the
# Employee object `e`.
# print(e.name,e.salary)
# print(str(e))
# print(repr(e))

print(len(e))
