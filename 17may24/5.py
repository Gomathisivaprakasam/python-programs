class Employee:
   count=0
   def __init__(self,name,age):
      self.__name=name
      self.__age=age
      Employee.count +=1
   def showcount(self):
      print(self.count)
   counter=classmethod(showcount)
e1=Employee("x",10)
e2=Employee("y",20)
e3=Employee("z",30)
Employee.counter()
