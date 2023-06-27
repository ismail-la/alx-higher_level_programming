#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    """Divides two lists element by element.
    """
    
    List_new = []
    for i in range(0, list_length):
        try:
            Divide = my_list_1[i] / my_list_2[i]
        except TypeError:
            print("wrong type")
            Divide = 0
        except ZeroDivisionError:
            print("division by 0")
            Divide = 0
        except IndexError:
            print("out of range")
            Divide = 0
        finally:
            List_new.append(Divide)
    return List_new
