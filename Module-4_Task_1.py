#factorial

def fact(x):
    if x<2:
        return 1
    else:
        return x*(fact(x-1))
    
result=fact(5)
print("factorial of x is:",result)