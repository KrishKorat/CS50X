#include <cs50.h>
#include <stdio.h>

int get_positive_num();

int main()
{

    int n = get_positive_num();
    int space = n - 1;
    int count = 1;

    for (int i = 0; i < n; i++)
    {
        for (int k = space; k > 0; k--)
        {
            printf(" ");
        }
        for (int j = 0; j < count; j++)
        {
            printf("#");
        }

        printf("\n");
        count++;
        space--;
    }
}

int get_positive_num()
{

    int n;
    do
    {
        n = get_int("Height: ");
    }
    while (n < 1);

    return n;
}
