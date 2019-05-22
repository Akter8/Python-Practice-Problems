string = input()
stringl = string.split()
dic = {}
for word in stringl:
    count = 0
    for word1 in stringl:
        if word == word1:
            count += 1
    dic.update({word:count})

for x in dic:
    print(x,dic[x])