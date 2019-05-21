n = int(input("Enter a number\n"))
ans = 0
count = 0
while n>0:
    x = n%10
    n = n//10
    x = x+1
    if x==10:
        x = 0
    ans = ans * 10 + x
    count = count + 1

while ans>0:
    x = ans%10
    ans = ans // 10
    print(x,end='')
    count = count - 1

while count!=0:
    print(0,end='')
    count = count - 1
