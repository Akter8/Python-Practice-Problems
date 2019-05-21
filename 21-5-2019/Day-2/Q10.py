def palindrome(a,l,r):
    m = (l+r)//2
    for i in range(m-l):
        if a[l+i] != a[r-(l+i)]:
            return False
    return True


string = input("Enter a word:\n")
stringl = list(string)
count = 0
for i in range(len(stringl)):
    for j in range(i,len(stringl)):
        if palindrome(stringl,i,j)==True:
            print(stringl[i:j])
            count += 1
print("The palindrome count is: "+str(count))