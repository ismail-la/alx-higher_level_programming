#!/usr/bin/python3

if __name__ == "__main__":
    from sys import argv
    Total_arg = 0
    num_arg = len(argv)

    for x in range(1, num_arg):
        Total_arg += int(argv[x])

    print(Total_arg)
