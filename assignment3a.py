#factorial
n=int(input("enter the number:"))

def factorial(f):
    if f==0:
        return 1
    else:
        return f*factorial(f-1)
print("the value of " , n,"!", factorial(n))