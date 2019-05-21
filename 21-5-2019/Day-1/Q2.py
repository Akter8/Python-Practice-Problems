x = input("Enter a number\n")
ans = 0
for i in range(1,int(x)+1):
    ans = ans + float(1/int(i))
print(float(ans))