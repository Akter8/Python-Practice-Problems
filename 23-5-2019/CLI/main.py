import xlwt
import xlrd
import cryptography as cpt
import string as s
import os
import colorama
import getpass
import myFunctions as mf

while 1:
    pref = mf.mainScreen()

    if pref == 1:
        mf.addUser()
    elif pref == 2:
        mf.signIn()
    else:
        break

