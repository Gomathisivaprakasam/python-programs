S = "school of linux"
a = ""
for i in S:
    if i not in a:
        a+=i
print(len(a))
