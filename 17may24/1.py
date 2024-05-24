class Employee:
   count=0
   def __init__(self,name,salary):
    self.name=name
    self.salary=salary
    Employee.count +=1
   def displaycount(self):
      print("Total Employee %d" % Employee.count)
   def displayEmployee(self):
      print("Name:",self.name, "salary:",self.salary)
emp1=Employee("sl",2000)
emp2=Employee("Linux",5000)
emp1.displayEmployee()
emp2.displayEmployee()
print("Total Employee %d" % Employee.count)
