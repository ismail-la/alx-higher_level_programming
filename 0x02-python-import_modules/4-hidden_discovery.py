#!/usr/bin/python3

if __name__ == "__main__":
    import hidden_4
    Names = dir(hidden_4)

    for name in Names:
        if "__" not in name:
            print(name)
