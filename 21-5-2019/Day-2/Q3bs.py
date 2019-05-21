def bs(integers):
    for j in range(len(integers)):
        for i in range(len(integers)-1):
            if integers[i]>integers[i+1]:
                temp = integers[i]
                integers[i] = integers[i+1]
                integers[i+1] = temp

print("Enter a few numbers to sort using bubble sort")
integers = [int(x) for x in input().split()]
bs(integers)
print(integers)