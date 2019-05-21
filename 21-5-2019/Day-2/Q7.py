string = input("Enter a few words\n")
stringlist = string.split()
wordcount = {}

for word in stringlist:
    count = 0
    for word2 in stringlist:
        if word==word2:
            count += 1
    
    wordcount.update({word:count})

for x in wordcount:
    print(x,end=' ')
    print(wordcount[x])