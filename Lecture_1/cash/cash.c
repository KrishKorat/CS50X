#include <cs50.h>
#include <stdio.h>

int get_positive_amt();

int main()
{

    int change = get_positive_amt();
    int coins = 0;

    while (change > 0)
    {

        if (change >= 25)
        {
            change -= 25;
            coins++;
            if (change < 10)
            {
                continue;
            }
        }
        else if (change >= 10)
        {
            change -= 10;
            coins++;
            if (change < 5)
            {
                continue;
            }
        }
        else if (change >= 5)
        {
            change -= 5;
            coins++;
            if (change < 1)
            {
                continue;
            }
        }
        else if (change >= 1)
        {
            change -= 1;
            coins++;
            if (change < 0)
            {
                continue;
            }
        }
    }
    printf("%i\n", coins);
}

int get_positive_amt()
{

    int change;
    do
    {
        change = get_int("Change owed: ");
    }
    while (change < 1);

    return change;
}
