def main():
    change = get_float()
    cents = round(change * 100)
    coin = chang(cents)
    print(coin)


def chang(change):
    coin = 0
    print(change)

    while change>0:

        if change>=25:
            change -= 25
            coin += 1

        elif change>=10:
            change -= 10
            coin += 1

        elif change>=5:
            change -= 5
            coin += 1

        elif change>=1:
            change -= 1
            coin += 1

    return coin


def get_float():
    while True:
            try:
                n = float(input("Change: "))
                if n>=0:
                    return n
                else:
                    continue
            except ValueError:
                continue


main()
