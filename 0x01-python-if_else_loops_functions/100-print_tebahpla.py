#!/usr/bin/python3
for i in range(ord('z'), ord('a')-1, -1):
    if i % 2 == 0:
        up = 0
    else:
        up = 32
    print('{}'.format(chr(i - up), end='')
