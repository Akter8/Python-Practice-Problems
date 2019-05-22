def my_gen(n):
    for i in range(n+1):
        if i%2==0:
            yield i
ans = []
n = int(input("Please enter a number:\n"))
for i in my_gen(n):
    ans.append(i)
print(ans)