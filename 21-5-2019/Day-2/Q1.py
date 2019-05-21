def max(int_list):
    my_list = int_list.split()
    max = my_list[0]
    second = my_list[0]
    for i in my_list:
        if i > max:
            max = i

    for i in my_list:
        if i > second and i < max:
            second = i
    return(second)
    

int_list = (input("Enter an array of numbers with spaces in between\n"))
print(max(int_list))