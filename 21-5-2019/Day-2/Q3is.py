def isort(a):
    for i in range(len(a)):
        for j in range(i,0,-1):
            while a[j]<a[j-1] and j>0:
                temp = a[j]
                a[j] = a[j-1]
                a[j-1] = temp


print("Enter a few numbers to sort")
a = [int(x) for x in input().split()]
isort(a)
print(a)