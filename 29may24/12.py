class employee:
   def __init__(self,name,age):
      self.__name = name
      self.__age = age
   def get_name(self):
      return (self.__name)
   def get_age(self):
      return (self.__age)
   def set_name(self,name):
      self.__name = name
      return
   def set_age (self,age):
      self.__age = age
e1 = employee("xyz",10)
print("Name:",e1.get_name(),"age:",e1.get_age())	
e1.set_name("Gomathi")
e1.set_age(27)
print("Name:",e1.get_name(),"age:",e1.get_age())
