def (n):
    if n < 0:
        return 0
    elif n ==0:
        return 1
    else:
        fact = 1 
        while(n>1):
            fact *=n
            n -= 1
            return fact
        num = 5
        print(num,factorial(num))
    
