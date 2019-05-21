import random as r
a = r.randint(0,9)
b = r.randint(0,9)
while 1:
    c = r.randint(0,9)
    if c == abs(a-b):
        break
while 1:
    d = r.randint(0,9)
    if d == (a+c)%10:
        break
print(a,b,c,d)