class Employee:
    company="Asus" # This is class attribute
    
    def __init__(self,salary,name,bond,comapny):
        self.salary=salary # Create  a instance attribute of name salary and assign it with salary
        self.name=name
        self.bond=bond
        self.company=comapny
  
    
    def get_salary(self): 
      return self.salary
  
    def get_info(self):
        return f"The name of the employee is {self.name}. Salary is Rs:{self.salary}/= The bond is for {self.bond} years"

e1=Employee(34000,"John Doe",4,"Tesla")
print(e1.company) # will always print instance attribute whenever present
print(Employee.company)  # This will always print class attribute

# Object introspection
#print(dir(e1))
    