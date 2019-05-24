import hashlib
import os

with open('salt.txt','wb') as f:
    f.write(salt)
f.close()

file = open('salt.txt','rb')
salt = file.read()
file.close()
print(salt)