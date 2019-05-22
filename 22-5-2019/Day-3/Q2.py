a = [int(x) for x in input().split()]
b = [int(x) for x in input().split()]
c = map(lambda x,y: x+y, a, b)
print(list(c))