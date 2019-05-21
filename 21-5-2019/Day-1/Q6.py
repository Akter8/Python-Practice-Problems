m = input("Enter a number\n")
n = int(m)
while n>0:
    x = n%10
    print(x,end='')
    n=int(int(n)/10)