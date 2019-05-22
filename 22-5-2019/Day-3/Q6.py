def bc(x,y):
    res = 1
    if y>x-y:
        y=x-y
    for i in range(y):
        res = res * (x-i)
        res = res // (i+1)
    return res

n = int(input("Enter the number of levels in the triangle\n"))
mat = [[0 for x in range(n)] for x in range(n)]



for row in range(n):
    #print(' ',end='')
    for i in range(n-row):
        print(' ',end='')
    for i in range(row+1):
        print(bc(row,i),' ',end='')
    print(' ')