def RandomOrder(int_list):
    max = int(int_list[0])
    min = int(int_list[0])
    for l in int_list:
        i = int(l)
        if i > max:
            max = i
        if i < min:
            min = i
    
    for i in range(min,max+1):
        if str(i) not in int_list:
            print(i)
            break



integers = input("Enter a set of integers with a space in between\n")
int_list = integers.split()
RandomOrder(int_list)