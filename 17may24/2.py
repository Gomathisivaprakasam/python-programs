class Employee:
   count=0
   def __inti__(self,name,salary):
    self.name=name
    self.salary=salary
    Employee.count +=1
   def displayEmployee(self):
      print("Name:",self.name, "salary:",self.salary)
print("Employee.__doc__:",Employee.__doc__)
print("Employee.__dict__:",Employee.__dict__)
print("Employee.__name__:",Employee.__name__)
print("Employee.__module__:",Employee.__module__)
print("Employee.__bases__:",Employee.__bases__)     
