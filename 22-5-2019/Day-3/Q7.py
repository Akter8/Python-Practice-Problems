string = input()
stringl = string.split()
dic = {}
for word in stringl:
    count = 0
    for word1 in stringl:
        if word == word1:
            count += 1
    dic.update({word:count})

maxi=0
mini=999
for x in dic:
    if dic[x]>maxi:
        maxi=dic[x]
        maxx=x
    if dic[x]<mini:
        mini=dic[x]
        minx=x

print("\nMax")
print(maxi,maxx)
print("Min")
print(mini,minx)
        