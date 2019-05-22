ans = []
inp = [(x) for x in input().split(',')]
for x in inp:
    if int(x)%5 == 0:
        ans.append(x)

print((','.join((ans))))
