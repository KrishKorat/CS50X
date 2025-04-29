def main():
    while True:
            try:
                n = int(input("Height: "))
                if n>0 and n<9:
                    mario(n)
                    break
                else:
                    continue
            except ValueError:
                continue


def mario(n):
    space = n-1
    count = 1

    for i in range(n):
        for j in range(space):
            print(" ", end="")
        for k in range(count):
            print("#", end="")
        print()
        space -= 1
        count += 1


main()
