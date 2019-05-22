cric = input("Enter cricket players:\n").split()
foot = input("Enter the football platers:\n").split()
bad = input("Enter the badminton players:\n").split()

al = []
one = []

for x in cric:
    if x in foot and x in bad:
        al.append(x)

for x in cric:
    if x not in foot and x not in bad:
        one.append(x)

for x in foot:
    if x not in cric and x not in bad:
        one.append(x)

for x in bad:
    if x not in foot and x not in cric:
        one.append(x)

print("All :")
print(al)

print("One :")
print(one)