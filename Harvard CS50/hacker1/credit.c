#include <stdio.h>
#include <cs50.h>


int cardlength(long long x);

int main(void)
{
    long long card;
    // get the card input from user
    do
    {
        printf("what is your credit card number?\n");
        card = get_long_long();
        if(card<=0)
        {
            printf("INVALID\n");
        }
    }
    while(card<0);
    
    //calculate the number of digits in the card number
    int num_digits = cardlength(card);
    
    //create the array to store the card number
    int card_array[num_digits];
    long long card1 = card;
    
    for(int i=0; i < num_digits; i++)
    {
        card_array[(num_digits - 1 - i)] = card1 % 10;
        card1 = card1 / 10;
    }
    
    //check to determine if the cards digits sum to a modulo 10 of 0
    int cardsum[(num_digits)];
    int cardsum1[(num_digits)];
    int totalsum = 0;
    int count = 0;
    
    //every other multiplied by 2
    for(int i = (num_digits - 2); i > -1; i = i - 2) 
    {
        int num = card_array[i] * 2;
        if(num > 9)
        {
            cardsum[count] = 1;
            cardsum[(count + 1)] = num % 10;
        } else {
            cardsum[count] = num;
            cardsum[(count + 1)] = 0;
        }
        count = count + 2;
    }
    
    count = 0;
    
    //remaining digits
    for(int i = (num_digits - 1); i > -1; i = i - 2) 
    {
        cardsum1[count] = card_array[i];
        cardsum1[(count + 1)] = 0;
        count = count + 2;
    }
    
    //sum total and detrmine modulo
    for(int i = 0; i < num_digits; i++)
    {
        totalsum = totalsum + cardsum[i] + cardsum1[i];
    }
    
    int check = 1;
    
    if(totalsum % 10 != 0) 
    {
        printf("INVALID\n");
        check = 0;
        
    }
    
    //check is to ensure this batch won't run if the modulo comes up to be something other than 0
    if(check == 1)
    {
        switch (num_digits)
        {
            case 13:
            if (card_array[0] == 4) 
            {
                printf("VISA\n");
            } else {
                printf("INVALID\n");
            }
            
            break;
            case 15:
            if (card_array[0] == 3 && (card_array[1] == 4 || card_array[1] == 7))
            {
                printf("AMEX\n");
            } else {
                printf("INVALID\n");
            }
            break;
            case 16:
            if (card_array[0] == 5 && (card_array[1] == 1 || card_array[1] == 2 || card_array[1] == 3 || card_array[1] == 4 || card_array[1] == 5))
            {
                printf("MASTERCARD\n");
            } else if (card_array[0] == 4) 
            {
                printf("VISA\n");
            } else {
                printf("INVALID\n");
            }
            break;
            default:
            printf("INVALID\n");
            break;
        }
    }
}

int cardlength(long long x)
{
    if(x>=100000000000) //12
    {
        if(x>=1000000000000000) return 16;
        if(x>=100000000000000) return 15;
        if(x>=10000000000000) return 14;
        if(x>=1000000000000) return 13;
        return 12;
    } else {
        if(x>=1000000) // 7
        {
            if(x>=10000000000) return 11;
            if(x>=1000000000) return 10;
            if(x>=100000000) return 9;
            if(x>=10000000) return 8;
            return 7;
        } else {
            if(x>=10) // 2
            {
                if(x>=100000) return 6;
                if(x>=10000) return 5;
                if(x>=1000) return 4;
                if(x>=100) return 3;
                return 2;
            } else {
                return 1;
            }
        }
    }
}