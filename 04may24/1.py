a = int(input("Enter a value : "))
b = int(input("Enter b value : "))

print("press 1 for addition")
print("press 2 for subtraction")
print("press 3 for multiplication")
print("press 4 for division")
print("press 5 for module")
print("press 6 for exit")

c = int(input())

if(c == 1):
  print(a+b)
if(c == 2):
  print(a-b)
if(c == 3):
  print(a*b)
if(c == 4):
  print(a/b)
if(c == 5):
  print(a%b)
if(c == 6):
  exit(-1)
