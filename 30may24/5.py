class school:
   def func1(self):
      print("This function is in school")
class student1(school):
    def func2(self):
      print("This function is in student1")
class student2(school):
    def func3(self):
       print("This function is in student2")
class student3(student1,student2,school):
    def func4(self):
       print("This function is in student3")
object = student3()
object.func1()
object.func2()
object.func3()
