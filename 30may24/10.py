class india():
   def capital(self):
      print("new dhile is the capital of india")
   def language(self):
      print("hindi is the most widely spoke language of india")
   def type(self):
      print("india is developing country")
class USA():
   def capital(self):
      print("washington is the captial of USA")
   def language(self):
      print("english is the primary language of USA")
   def type(self):
      print("USA is developed country")
def func(obj):
   obj.capital()
   obj.language()
   obj.type()
obj_ind = india()
obj_usa = USA()
func(obj_ind)
func(obj_usa)
