def cub(x):
    return(x*x*x)

n = input("Enter a number\n")
ans = 0
for i in range(1,int(n)+1):
    ans = ans + float(1/cub(i))
print(float(ans))

