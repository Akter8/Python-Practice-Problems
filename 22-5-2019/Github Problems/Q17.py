amt = 0
while 1:
    inp = input()
    if inp:
        if inp[0]=='D':
            amt += int(inp[2:len(inp)])
        else:
            amt -= int(inp[2:len(inp)])
    else:
        break

print(amt)