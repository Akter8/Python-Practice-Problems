def my_gen(n):
    i=1
    while i<=n:
        if i%7==0 and i%5==0:
            yield i
        i += 1
    
ans = []
n = int(input("Please enter a number:\n"))
for i in my_gen(n):
    ans.append(i)
print(ans)