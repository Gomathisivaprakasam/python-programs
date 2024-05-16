digits = [str(x) for x in range(10)]
mystr = 'HE234LLO, PY948TH23O'
chars = []
for x in mystr:
   if x not in digits:
      chars.append(x)
newstr = ''.join(chars)
print (newstr)
