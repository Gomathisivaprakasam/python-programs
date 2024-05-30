class parent:
   def func1(self):
      print("This is parent process")
class child(parent):
   def func2(self):
      print("This is child process")
object = child()
object.func1()
object.func2()
