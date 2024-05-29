class scl:
   def __init__(self,name="linux",age = 24):
      self.name = name
      self.age = age
   def diplayscl(self):
      print("name :",self.name,"age:",self.age)
print(scl.__doc__)
print(scl.__name__)
print(scl.__module__)
print(scl.__dict__)
