def permute(a,l,r):
    if l==r:
        print(a)
    else:
        for i in range(l,r+1):
            temp = a[l]
            a[l] = a[i]
            a[i] = temp
            permute(a, l+1, r)
            temp = a[l]
            a[l] = a[i]
            a[i] = temp

string = str(input("Enter a word:\n"))
n = len(string)
stringl = list(string)
permute(stringl,0,n-1)