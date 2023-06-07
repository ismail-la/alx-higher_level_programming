#!/usr/bin/python3

for charr in range(97, 123):
    if chr(charr) is not 'q' and chr(charr) is not 'e':
        print("{}".format(chr(charr)), end="")
