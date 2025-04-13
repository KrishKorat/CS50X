#include <cs50.h>
#include <ctype.h>
#include <stdio.h>
#include <string.h>

int main(void)
{
    string p1 = get_string("Player 1: ");
    string p2 = get_string("Player 2: ");

    int s1 = 0;
    int s2 = 0;

    for (int i = 0, len1 = strlen(p1); i < len1; i++)
    {
        p1[i] = tolower(p1[i]);
        char c = p1[i];

        if (c == 'a' || c == 'e' || c == 'i' || c == 'l' || c == 'n' || c == 'o' || c == 'r' ||
            c == 's' || c == 't' || c == 'u')
        {
            s1 += 1;
            continue;
        }
        else if (c == 'd' || c == 'g')
        {
            s1 += 2;
            continue;
        }
        else if (c == 'b' || c == 'c' || c == 'm' || c == 'p')
        {
            s1 += 3;
            continue;
        }
        else if (c == 'f' || c == 'h' || c == 'v' || c == 'w' || c == 'y')
        {
            s1 += 4;
            continue;
        }
        else if (c == 'k')
        {
            s1 += 5;
            continue;
        }
        else if (c == 'j' || c == 'x')
        {
            s1 += 8;
            continue;
        }
        else if (c == 'q' || c == 'z')
        {
            s1 += 10;
            continue;
        }
    }

    for (int i = 0, len2 = strlen(p2); i < len2; i++)
    {
        p2[i] = tolower(p2[i]);
        char c = p2[i];

        if (c == 'a' || c == 'e' || c == 'i' || c == 'l' || c == 'n' || c == 'o' || c == 'r' ||
            c == 's' || c == 't' || c == 'u')
        {
            s2 += 1;
            continue;
        }
        else if (c == 'd' || c == 'g')
        {
            s2 += 2;
            continue;
        }
        else if (c == 'b' || c == 'c' || c == 'm' || c == 'p')
        {
            s2 += 3;
            continue;
        }
        else if (c == 'f' || c == 'h' || c == 'v' || c == 'w' || c == 'y')
        {
            s2 += 4;
            continue;
        }
        else if (c == 'k')
        {
            s2 += 5;
            continue;
        }
        else if (c == 'j' || c == 'x')
        {
            s2 += 8;
            continue;
        }
        else if (c == 'q' || c == 'z')
        {
            s2 += 10;
            continue;
        }
    }

    if (s1 > s2)
    {
        printf("Player 1 wins!\n");
    }
    else if (s1 < s2)
    {
        printf("Player 2 wins!\n");
    }
    else
    {
        printf("Tie!\n");
    }
}
