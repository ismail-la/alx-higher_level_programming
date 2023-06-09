#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    arg_count = len(argv)

    if arg_count == 1:
        print("{} arguments.".format(0))
    elif arg_count == 2:
        print("{} argument:".format(1))
    else:
        print("{} arguments:".format(arg_count - 1))

    if arg_count > 1:
        for x in range(1, arg_count):
            print("{}: {}".format(x, argv[x]))
