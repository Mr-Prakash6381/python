def exfact(n):
    if(n==1):
        return (1)
    else:
         return (n*exfact(n-1))

n=3
print("Factorial=",exfact(n))
