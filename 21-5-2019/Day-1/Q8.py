m = int(input("Enter a base\n"))
n = int(input("Enter an exponent\n"))
ans = 1
for i in range(0,n):
    ans = ans * m
print("m to the power n is: " + str(ans))