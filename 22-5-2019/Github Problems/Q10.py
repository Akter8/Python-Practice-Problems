inp = []
while 1:
    inpu = input()
    if inpu == '':
        break
    else:
        inp.append(inpu)

for i in inp:
    print(i.upper())