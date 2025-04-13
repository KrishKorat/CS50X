#include <cs50.h>
#include <math.h>
#include <stdio.h>
#include <string.h>

int main(void)
{
    string text = get_string("Text: ");
    int letters = 0;
    int words = 1;
    int sentences = 0;

    for (int i = 0, len = strlen(text); i < len; i++)
    {

        if (text[i] != ' ')
        {
            if (text[i] >= 'a' && text[i] <= 'z')
            {
                letters++;
            }
            else if (text[i] >= 'A' && text[i] <= 'Z')
            {
                letters++;
            }
        }
        if (text[i] == ' ')
        {
            words++;
        }
        if (text[i] == '.' || text[i] == '!' || text[i] == '?')
        {
            sentences++;
        }
    }

    float L = ((float) letters / words) * 100;
    float S = ((float) sentences / words) * 100;

    float index = 0.0588 * L - 0.296 * S - 15.8;
    int rIndex = round(index);

    if (rIndex < 1)
    {
        printf("Before Grade 1\n");
    }
    else if (rIndex > 16)
    {
        printf("Grade 16+\n");
    }
    else
    {
        printf("Grade %i\n", rIndex);
    }
}
