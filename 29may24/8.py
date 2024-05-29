class scl:
   def __init__(self,name = "Linux",age = 29):
      self.name = name
      self.age = age
   def displayscl(self):
      print("name:",self.name,"age:",self.age)
e1 = scl()
e2 = scl("gomathi",29)
e1.displayscl()
e2.displayscl()
