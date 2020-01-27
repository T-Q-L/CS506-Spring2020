def draw_school(length = 0):
    add_dot(length)
    print("...^...", end="")
    add_dot(length)
    print()

    add_dot(length)
    print("../.\..", end="")
    add_dot(length)
    print()

    add_line(length)
    print("_....._", end="")
    add_line(length)
    print()

    print("|", end="")
    add_dot(length)
    print(".....", end="")
    add_dot(length)
    print("|")

    print("|", end="")
    add_dot(length)
    print(".....", end="")
    add_dot(length)
    print("|")

    print("|", end="")
    add_dot(length)
    print("_____", end="")
    add_dot(length)
    print("|")
        
    print("|", end="")
    add_line(length)
    print("|...|", end="")
    add_line(length)
    print("|")
    return

def add_dot(length = 0):
    for i in range(length):
        print(".", end="")
    return

def add_line(length = 0):
    for i in range(length):
        print("_", end="")
    return