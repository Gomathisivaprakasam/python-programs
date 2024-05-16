mystr = '111111'
def strtoint(mystr):
    for x in mystr:
        if x not in '01': return "Error"
    num = int(mystr,2)
    return num
print(mystr,strtoint(mystr))
