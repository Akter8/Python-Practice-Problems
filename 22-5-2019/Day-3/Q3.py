import functools as f
def sumi(x,y):
    return x+y
a = [int(x) for x in input().split()]
su = f.reduce(sumi,a)
print(su)