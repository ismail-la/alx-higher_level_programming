#!/usr/bin/python3

def multiple_returns(sentence):
    if sentence != '':
        first_charr = sentence[0]
    else:
        first_charr = None
    return (len(sentence), first_charr)
