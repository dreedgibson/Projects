#include <stdio.h>
#include <cs50.h>
#include <string.h>
#include <ctype.h>

// initial function declaration
void find_init(string name);

int main(void)
{
    //Request in input of name from user
    string name = GetString();
    
    //Call function
    find_init(name);
}

void find_init(string name)
{
    int j = 0; //counter used to print initials
    for(int i = 0, n = strlen(name); i <= n; i++)
    {
        if(name[i] == 32 || name[i] == 0)
        {
            printf("%c", toupper(name[j]));
            j = i + 1; //This works assuming there is only one space between names
        }
    }
    printf("\n");
}