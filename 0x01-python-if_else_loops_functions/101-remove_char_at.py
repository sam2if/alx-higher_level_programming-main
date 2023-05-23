#!/usr/bin/python3
def remove_char_at(str, n):
    final = ""
    for i in range(0, len(str)):
        if i != n:
            final = final + str[i]
    return final
