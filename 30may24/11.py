class animal:
   def speak(self):
      return nothing
class dog(animal):
   def speak(self):
      return "woof"
class cat(animal):
   def speak(self):
      return "meow"
animals = [dog(), cat()]
for animal in animals:
   print(animal.speak())
