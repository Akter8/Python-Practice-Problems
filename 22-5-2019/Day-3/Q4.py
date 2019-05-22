import functools as f

def fil(x):
    if x%2==0:
        return True
    else:
        return False

a = [int(x) for x in input().split()]
filtered = filter(fil, a)
b = list(filtered)

squares = map(lambda x: x*x, b)
c = list(squares)

sumi = f.reduce(lambda x,y: x+y, c)
print(sumi)