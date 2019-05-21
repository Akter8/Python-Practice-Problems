x = int(input("Enter a number\n"))
print("Enter a few numbers")
a = [int(x) for x in input().split()]
flag = False
for i in a:
    if i==x:
        flag = True
        break

print(flag)