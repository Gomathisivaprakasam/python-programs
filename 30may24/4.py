class parent:
   def func1(self):
      print("This function is parent")
class child1(parent):
   def func2(self):
      print("This is child1")
class child2(parent):
    def func3(self):
       print("This is child2")
object1 = child1()
object2 = child2()

object1.func1()
object1.func2()
object2.func1()
object2.func3()
