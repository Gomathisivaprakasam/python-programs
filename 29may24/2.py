 class employee:
   def showcount(cls):
        print(cls.empcount)
	 return
   def newemployee(cls,name,age):
         return cls(name,age)
e1 = Employee("scl",24)
e2 = Employee("linux",36)
e3 = Employee("jai",6)
e4 = Employee.newemployee("gomathi",27)
