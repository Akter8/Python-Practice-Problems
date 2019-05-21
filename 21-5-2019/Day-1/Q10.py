n = int(input("Enter a number:\n"))

for j in range(0,n):
    for i in range(0,n-j):
        print(' ',end='')

    for i in range(0,j):
        print(i+1,end='')

    for i in range(j,-1,-1):
        print(i+1,end='')

    print(" ")

