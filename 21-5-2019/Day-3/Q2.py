import random as r

def sumi(inp):
    sum = 0
    for i in inp:
        sum = sum + i
    return sum

def maxi(inp):
    maxa = inp[0]
    for i in inp:
        if i>maxa:
            maxa=i
    return maxa

def mini(inp):
    mina = inp[0]
    for i in inp:
        if i<mina:
            mina=i
    return mina

def reversedi(inp):
    reverse = [0]*len(inp)
    for i in range(len(inp)-1,-1,-1):
        reverse[len(inp)-i-1] = inp[i]
    return reverse

def search(x,inp):
    if x in inp:
        return True
    else:
        return False

def shuffle(inp):
    for i in range(len(inp)):
        x = r.randint(i,len(inp)-1)
        temp = inp[i]
        inp[i] = inp[x]
        inp[x] = temp

def avg(a):
    return sumi(a)/len(a)


print("Enter an array of numbers")
inputs = [int(x) for x in input().split()]
print(inputs)
print("Sum is: " + str(sumi(inputs)))
print("Max is: " + str(maxi(inputs)))
print("Min is: " + str(mini(inputs)))
print("Avg is: " + str(avg(inputs)))
print("Reversed List is: ")
print(reversedi(inputs))
print("Shuffled list is:")
shuffle(inputs)
print(inputs)

x = int(input("Enter a number to search in the list\n"))
print(search(x,inputs))

