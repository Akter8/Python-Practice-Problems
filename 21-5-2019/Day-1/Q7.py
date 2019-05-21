n = int(input("Enter a number:\n"))
sum = n
while n//10>0:
    n = sum
    sum = 0
    while n>0:
        x = n%10
        n = n//10
        sum = sum + x
    print(sum)
    n = sum