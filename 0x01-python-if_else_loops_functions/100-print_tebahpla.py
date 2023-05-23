#!/usr/bin/python3
for i in range(0, 26):
    if i % 2 == 0:
        ch = 122 - i
    else:
        ch = 122 - i - 32
    print("{:c}".format(ch), end='')
