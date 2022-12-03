import re

while True:
    test = input("A:")

    if not (re.match("^[A-Z]{4}$",test) == None):
        print(test)