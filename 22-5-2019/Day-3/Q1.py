def function(letter):
    vowels = ['a','e','i','o','u']
    if letter in vowels:
        return True
    else:
        return False

sequence = input("Please enter a string:\n")
ans = filter(function,sequence)
print(list(ans))
ans = filter(function,sequence)
print(len(list(ans)))
