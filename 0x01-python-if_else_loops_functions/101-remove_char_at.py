#!/bin/usr/python3
def remove_char_at(str, n):
    if n < 0:
        return (str)
    else:
        return (str[:n] + str[n + 1:])
