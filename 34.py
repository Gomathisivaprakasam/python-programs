mystr = "All animals are equal .Some are more equal"
Vowels = "aeiou"
count = 0
for x in mystr:
    if x.lower() in Vowels:
        count +=1
print(count)
