import math
n=int(input('enter the number'))
print('if you want "square root" or "log" or "sine" of the number then enter "sq-root" or "log" or "sine"' )

takein = input('enter your choice:')

def userinput(q):

    if q == 'sq-root':
        return  math.sqrt(n)
    elif q == 'l':
        return math.log(n)
    elif q == 'sin':
        return math.sin(n)
    else :
        return 'invalid choice'

print(userinput(takein))
