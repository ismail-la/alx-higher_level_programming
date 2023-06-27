#!/usr/bin/python3

def safe_print_division(a, b):
    """Returns the division of a by b."""

    try:
        Division = a / b
    except (TypeError, ZeroDivisionError):
        Division = None
    finally:
        print("Inside result: {}".format(Division))
    return Division
