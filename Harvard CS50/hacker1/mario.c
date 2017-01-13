#include <stdio.h>
#include <cs50.h>



int main(void)
{
    int block_height;
    int check = 0;
    do
    {
        printf("Height of Pyramid between 0 and 23 blocks:");
        block_height = get_int();
        if(block_height >= 0 && block_height<= 23) check = 1;  
    }
    while(check == 0);

    int i, j, k, l, m;
    
    for(i=1; i <= block_height; i++)
    {
        for(j= 1; j <= (block_height - i); j++)
        {
            printf(" ");
        }
        for(k=1; k<=i; k++)
        {
            printf("#");
        }
        for(l = block_height+1; l <= block_height + 2; l++)
        {
            printf(" ");
        }
        for(m = block_height + 2; m < block_height + 2 + i; m++)
        {
            printf("#");
        }
        printf("\n");
    }
}
