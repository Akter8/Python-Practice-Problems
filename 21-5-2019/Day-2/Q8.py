string = input("Enter a string\n")
vowels = ['a','e','i','o','u']
vcount = 0
ccount = 0
for letter in string:
    if letter in vowels:
        vcount += 1
    else:
        ccount += 1
print("Vowel count is: " + str(vcount) + " And the consonant count is: " + str(ccount))