x = input("Enter a number\n")
prime = True
for i in range(2,int(x)):
    if int(x)%i == 0:
        prime = False
        break

if prime == True:
    print("It is a prime")
else:
    print("It is not a prime")
