class grandfather:
   def __init__(self,grandfathername):
      self.grandfathername = grandfathername
class father(grandfather):
   def __init__(self,fathername,grandfathername):
      self.fathername = fathername
      grandfather.__init__(self,grandfathername)
class son(father):
   def __init__(self, sonname, fathername, grandfathername):
      self.sonname = sonname
      father.__init__(self, fathername, grandfathername)
   def print_name(self):
      print("grandfathername : ", self.grandfathername)
      print("fathername :", self.fathername)
      print("sonname :", self.sonname)
s1 = son('jai','siva','ramachandran')
print(s1.grandfathername)
s1.print_name()
