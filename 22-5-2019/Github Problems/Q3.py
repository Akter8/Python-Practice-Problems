n = int(input("Enter a number:\n"))
dic = {}
for i in range(1,n+1):
    dic.update({i:i*i})
print(dic)