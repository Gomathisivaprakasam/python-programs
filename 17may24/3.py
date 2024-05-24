class point:
   def __init__(self,x=0,y=0):
      self.x=x
      self.y=y
   def __del__(self):
    class_name=self.__class__.__name__
    print(class_name,"destroyed")
ptr1=point()
ptr2=ptr1
ptr3=ptr1
print(id(ptr1),id(ptr2),id(ptr3))
del ptr1
del ptr2
del ptr3
