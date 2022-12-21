import random as r
import string as strg
from time import sleep as slp
import os


def error():
    print("Error")
    slp(2)
    exit()

def clr():
    os.system('cls')

def yOrN():
    print("\n[Y] Yes")
    print("[N] No\n")

def dataPrint():
    print("Length:", length)

    if decidePnct == "Y" or decidePnct == "y":
        print("Punctuation: Yes")

    elif decidePnct == "N" or decidePnct == "n":
        print("Punctuation: None")
    else:
        error()


lower = strg.ascii_lowercase
upper = strg.ascii_uppercase
num = strg.digits
pun = strg.punctuation


print("version 1.15-c.1")
slp(1)
clr()

print("Password generator by @kmtrebacz")

print("\nHow many characters do you want in your password?")
print("Min length: 6\nMax lenght:62\n")
length = int(input("->"))

clr()

if length <= 62 and length > 4:

    print("\nDo you want punctuation in your password?")
    yOrN()
    decidePnct = str(input("->"))

    if decidePnct == "Y" or decidePnct == "y":

        all = lower + upper + num + pun

        temp = r.sample(all, length)

        passwordWith = "".join(temp)

        clr()

        dataPrint()
        print("\nYour password is:")
        print(passwordWith)

        slp(1)

    elif decidePnct == "N" or decidePnct == "n":

        all = lower + upper + num

        temp = r.sample(all, length)

        passwordWithout = "".join(temp)

        clr()

        dataPrint()
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