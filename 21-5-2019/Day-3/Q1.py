def palindrome(x):
    a = 0
    b = x
    while x>0:
        a = a*10 + x%10
        x = x//10
    while a>0:
        c = a%10
        d = b%10
        if c!=d:
            return False
        a = a//10
        b = b//10
    return True

def factorial(x):
    ans = 1
    for i in range(1,x+1):
        ans = ans * i
    return ans

def GCD(x,y):
    gcd = 1
    for i in range(1,min(x,y)):
        if x%i==0 and y%i==0:
            gcd = i
    return gcd

x = int(input())
y = int(input())
print(palindrome(x))
print(palindrome(y))
print(GCD(x,y))
print(factorial(x))
print(factorial(y))