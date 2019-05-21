n = int(input("Enter the number of rows:\n"))
m = int(input("Enter the number of colums:\n"))
arr = [[0 for x in range(n)] for x in range(m)]
print("Enter the numbers rowwise")
colmin = []
colmax = []
rowmin = []
rowmax = []

for i in range(n):
    mini = 9999
    maxi = 0
    for j in range(m):
        arr[i][j] = int(input())
        if arr[i][j] >maxi:
            maxi = arr[i][j]
        if arr[i][j] < mini:
            mini = arr[i][j]
    rowmax.append(maxi)
    rowmin.append(mini)

print("Rowmin")
print(rowmin)
print("Rowmax:")
print(rowmax)

maxi = rowmax[0]
for i in rowmax:
    if i > maxi:
        maxi = i
mini = rowmin[0]
for i in rowmin:
    if i < mini:
        mini = i

print("Maximum is: "+str(maxi))
print("Minimum is: "+str(mini))

for i in range(n):
    maxi = arr[0][i]
    mini = arr[0][i]
    for j in range(m):
        if arr[j][i] > maxi:
            maxi = arr[j][i]
        if arr[j][i] < mini:
            mini = arr[j][i]
    colmax.append(maxi)
    colmin.append(mini)

print("Colmin")
print(colmin)
print("Colmax:")
print(colmax)