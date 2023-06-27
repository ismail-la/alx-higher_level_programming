#!/usr/bin/python3
def magic_calculation(a, b):
    """ Write the Python function def magic_calculation(a, b):
    """
    Resultat = 0
    for j in range(1, 3):
        try:
            if j > a:
                raise Exception('Too far')
            Resultat += a ** b / j
        except Exception:
            Resultat = b + a
            break
    return Resultat
