n = int(input("Enter the order of the matrix\n"))
a = [[0 for x in range(n)] for x in range(n)]

for i in range(n):
    a[i][i]=1

for i in range(len(a)):
    for j in a[i]:
        print(j,end='')
    print()