#include <stdio.h>
#include <cs50.h>
#include <stdlib.h>
#include <string.h>

int main(void)
{
    string s = "1234567";
    int n = strlen(s);
    int num1[n];
    for(int i = 0; i < n; i++)
    {
        num1[i] = s[i] - 48;
    }
    
    int xx = num1[1] + 10;
    printf("%i\n", xx);
}