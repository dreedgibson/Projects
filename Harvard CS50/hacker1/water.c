#include <stdio.h>
#include <cs50.h>

int main(void)
{
    int minute;
    
    do 
    {
        printf("How long was your shower?\n");
        minute = get_int(); 
    }
    while(minute < 1);
    
    int bottles = minute * 12;
    
    printf("You used %i bottles of water to shower!\n", bottles);
}