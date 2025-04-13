#include <cs50.h>
#include <ctype.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

bool only_digits(string s);
char rotate(char c, int n);

int main(int argc, string argv[])
{

    if (argc != 2)
    {
        printf("Usage: ./caesar key\n");
        return 1;
    }
    else
    {
        string s = argv[1];
        
        if (only_digits(s))
        {

            int n = atoi(s);

            string plainText = get_string("plaintext: ");
            int len = strlen(plainText);
            char cipherText[len + 1];

            for (int i = 0; i < len; i++)
            {
                char c = plainText[i];
                cipherText[i] = rotate(c, n);
            }
            cipherText[len] = '\0';

            printf("ciphertext: %s\n", cipherText);

            return 0;
        }
        else
        {
            printf("Usage: ./caesar key\n");
            return 1;
        }
    }
}

bool only_digits(string s)
{

    for (int i = 0, len = strlen(s); i < len; i++)
    {
        if (isdigit(s[i]))
        {
            continue;
        }
        else
        {
            return false;
        }
    }
    return true;
}

char rotate(char c, int n)
{
    if (isupper(c))
    {
        return (char) (((c - 'A' + n) % 26) + 'A');
    }
    else if (islower(c))
    {
        return (char) (((c - 'a' + n) % 26) + 'a');
    }
    else
    {
        return c;
    }
}
