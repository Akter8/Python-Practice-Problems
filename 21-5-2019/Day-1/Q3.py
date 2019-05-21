x = input("Enter a number\n")
y = input("Enter another number greater than the previous one\n")
print("All the prime numbers between these two are:")
for i in range(int(x),int(y)+1):
    flag = True
    for j in range(2,int(i)):
        if i%j == 0:
            flag = False
            break
    if flag == True:
        print(str(i))