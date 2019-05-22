import csv
lis = []
with open('D:\SampleData.csv','rt') as f:
    data = csv.reader(f)
    count = 0
    for row in data:
        if count != 0:
            lis.append(row)
        else:
            count += 1
degree = {}
for x in lis:
    if x[4] in degree:
        degree.update({x[4]:degree[x[4]]+1})
    else:
        degree.update({x[4]:1})

print("\n\nDegree-wise number of students:")
maxi = 0
for x in degree:
    print(x,degree[x])


placed = 0
for x in lis:
    if x[3]=='Y':
        placed += 1

print("\n\nNumber of placed students is: "+ str(placed))

print("\n\n\n\nDetails of all students completed but not placed")
for x in lis:
    if x[2]=='Y' and x[3]=='N':
        print(x)

print("\n\n\nAscending order of names")
sort=sorted(lis,key=lambda x: x[0])
for x in sort:
    print(x)

maxi=0.0
mini=999.1
sumi=0.0
for x in lis:
    sumi += float(x[5])
    if float(x[5])>maxi:
        maxi=float(x[5])
    if float(x[5])<mini:
        mini=float(x[5])

print("\n\nMax Min Avg")
print(maxi,mini,sumi/len(lis))

top = []
count = 0
for x in lis:
    if count>=5:
        break
    top.append(x)
    count += 1


count=0
for x in lis:
    if count<5:
        count += 1
        continue
    top = sorted(top,key=lambda x: x[5])
    if x[5]>top[0][5]:
        top.pop(0)
        top.append(x)

print("\n\nToppers are:")
for x in reversed(top):
    print(x)