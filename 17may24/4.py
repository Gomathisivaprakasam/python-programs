class Employee:
   count=0
   def __init__(self,name,age):
      self.__name=name
      self.__age=age
      Employee.count +=1
      print("Name:",self.__name,"Age:",self.__age)
      print("Employee number:",Employee.count)
e1=Employee("a",24)
e2=Employee("b",30)
e3=Employee("c",46)
