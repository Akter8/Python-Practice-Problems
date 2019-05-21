def merge(a,l,m,r):
    n1 = m - l + 1
    n2 = r - m

    llist = [0]*(n1)
    for i in range(n1):
        llist[i]=(a[i+l])

    rlist = [0]*(n2)
    for i in range(n2):
        rlist[i]=(a[i+m+1])

    i = 0
    j = 0
    k=l
    while i<n1 and j<n2:
        if llist[i]<=rlist[j]:
            a[k] = llist[i]
            i = i + 1
            k = k + 1
        else:
            a[k] = rlist[j]
            j = j + 1
            k = k + 1
    
    while i<n1:
        a[k]=llist[i]
        k = k + 1
        i = i + 1

    while j<n2:
        a[k] = rlist[j]
        j = j + 1
        k = k + 1

def ms(a,l,r):
    if l<r:
        m = (l+r)//2
        ms(a,l,m)
        ms(a,m+1,r)
        merge(a,l,m,r)

print("Enter a few numbers to sort")
a = [int(x) for x in input().split()]
print(a)
ms(a,0,len(a)-1)
print(a)
