#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new = a_dictionary.copy()
    list_key = list(new())
    for i in list_key:
        new[i] = new[i] *  2
    return (new)
