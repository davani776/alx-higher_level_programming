#!/usr/bin/python3
def uppercase(s):
    result = ""
    for char in s:
        if 'a' <= char <= 'z':
            char = chr(ord(char) - ord('a') + ord('A'))
        result += char
    print("{}".format(result))
