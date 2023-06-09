#!/usr/bin/python3

def magic_calculation(a, b):
    from magic_calculation_102 import sub, add
    if a < b:
        s = add(a, b)
        for x in range(4, 6):
            s = add(s, x)
        return (s)

    else:
        return(sub(a, b))
