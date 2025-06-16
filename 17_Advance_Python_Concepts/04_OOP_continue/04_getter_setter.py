class Employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
    
    @property      # Encapsulation   it is a getter method
    def first_name(self):
         l=self.name.split(" ") # .split(" ") returns a list 
         #print(l)
         return l[0]
     
    @first_name.setter    # it is a setter method name should be same
    def first_name(self,a):
        l=self.name.split(" ")
        newname= f"{a} {l[1]}"
        self.name=newname
        

e=Employee("Jack Doe",34555)
# e.project=6
# print(e.project)     
#print(e.first_name())

# e.set_first_name("John")
# print(e.name)

# Done by using @property decorator
print(e.first_name)
e.first_name="John"
print(e.name)