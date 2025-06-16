class Employee:
    company="HP"
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
    
    #Instance Method (default)
    def print_info(self):
        info= f"The name is {self.name} and the salarly is {self.salary}"
        print(info)
    
    #def sum(self,a,b):
    #def sum(a,b): # Will not work throw an error
    @staticmethod   #Static Method
    def sum(a,b):
        return a+b
    
    #Class Methods
    @classmethod
    def print_company(cls):
        print(cls.company)

    @classmethod
    def change_company(cls,new_company):
        cls.company=new_company



e1=Employee("Jack",34500)
e2=Employee("Jill",34500)
#print(Employee.company) #class attribute
#print(Employee.name) # error : Instance Method
# e1.print_info()
 
# print(e2.sum(5,3))
#e1.print_company()
print(Employee.company)

e1.change_company("Acer")

#e1.print_company()
print(Employee.company)
