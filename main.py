import random as r
import string as strg
from time import sleep as slp
import os

def yOrN():
    print("\n[Y] Yes")
    print("[N] No\n")

def error():
    print("Error")
    slp(2)
    exit()

def clr():
    os.system('cls')


lower = strg.ascii_lowercase
upper = strg.ascii_uppercase
num = strg.digits
pun = strg.punctuation


print("version 1.16-c.1")
slp(1)
clr()

print("Password generator by @kmtrebacz")
print("Warning! Min length of password is 4 and max length 62")

print("\nHow many characters do you want in your password?")
length = int(input("->"))

if length <= 62 and length > 4:

    print("\nDo you want punctuation in your password?")
    yOrN()
    decidePnct = str(input("->"))

    if decidePnct == "Y" or decidePnct == "y":

        all = lower + upper + num + pun

        temp = r.sample(all, length)

        passwordWith = "".join(temp)

        clr()
        print("\nYour password is:")
        print(passwordWith)

        slp(1)

    elif decidePnct == "N" or decidePnct == "n":

        all = lower + upper + num

        temp = r.sample(all, length)

        passwordWithout = "".join(temp)

        clr()
        print("\nYour password is:")
        print(passwordWithout)

        slp(1)

    else:
        error()

else:
    print("Error")
    slp(2)
    exit()


input("\nTo end the program press 'Enter'")