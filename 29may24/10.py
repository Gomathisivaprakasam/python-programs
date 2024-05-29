class scl:
   def __init__(self,name,age,salary):
      self.name = name
      self.__age = age
      self.salary = salary
   def displayscl(self):
      print("name:",self.name,"age:",self.age,"salary:",self.salary)
e1 = scl("Linux",39,10000)
print(e1.name)
print(e1.age)
print(e1.salary)
