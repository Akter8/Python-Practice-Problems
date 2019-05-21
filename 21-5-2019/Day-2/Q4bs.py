x = int(input("Enter a number\n"))
print("Enter a few numbers")
a = [int(x) for x in input().split()]
l = 0
r = len(a)-1
while(l<r):
    m = (l+r)//2
    if a[m]==x:
        print(True)
        break
    elif a[m]<x:
        l = m
    else:
        r = m
