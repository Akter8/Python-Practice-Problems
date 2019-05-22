import string as s
def pass_checker(lis):
    ans = []
    small = 0
    big = 0
    number = 0
    special = 0
    sma = list(s.ascii_lowercase)
    bi = list(s.ascii_uppercase)
    num = list(s.digits)
    char = ['$','#','@']
    for passw in lis:
        for letter in passw:
            if letter in sma:
                small += 1
            elif letter in bi:
                big += 1
            elif letter in num:
                number += 1
            elif letter in char:
                special += 1
        
        if small>=1 and big>=1 and number>=1 and special >=1 and len(passw)>=6 and len(passw)<=12:
            ans.append(passw)
            #print(ans,number,special)

    return ans


stringlist = input("Enter a few passwords:\n")
lis = stringlist.split(',')
passw = pass_checker(lis)
print(passw)