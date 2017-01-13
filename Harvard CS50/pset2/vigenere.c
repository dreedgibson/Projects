#include <stdio.h>
#include <cs50.h>
#include <string.h>
#include <stdlib.h>
#include <ctype.h>

string cipher(string text, int start, int finish, int modulo, string keyword);

int main(int argc, string argv[])
{
    // return an error should there be an incorrect number of arguments
    if(argc != 2)
    {
        printf("Vigenere.c has one (1) command line input\n");
        return 1;
    }
    
    //declare variable for keyword
    string keyword = argv [1];
    
    // return an error should the keyword not be all alpha characters
    for(int i = 0, n = strlen(keyword); i < n; i++)
    {
        if(!isalpha(keyword[i]))
        {
            printf("Vigenere requires alpha charaacters\n");
            return 1;
        }
    }
    
    //sub step to ensure uniformity in ASCII values
    for(int i = 0, n =strlen(keyword); i < n; i++)
    {
        keyword[i] = toupper(keyword[i]);
    }
    
    //request input from user
    string plaintext = GetString();
    
    int start_upper = 65; //start and end of upper case ASCII numbers
    int end_upper = 90;
    int start_lower = 97; //start and end of lower case ASCII numbers
    int end_lower = 122;
    int total_char = 26; //total number of chars
    
    string cipher_text = cipher(plaintext, start_upper, end_upper, total_char, keyword); //change the upper case letters
    cipher_text = cipher(cipher_text, start_lower, end_lower, total_char, keyword); //change the lower case letters
    
    //print the final encrypted text
    printf("%s\n", cipher_text);
    
    return 0;
}

//function to encode the text 
string cipher(string text, int start, int finish, int modulo, string keyword)
{
    int key_char = 0; //initialize the first word of keychar
    int start_key = 65; //A in ASCII
    int punc_start = 32; //accounting for the various punctuation in the string.
    int punc_fin = 64;
    
    for(int i = 0, n = strlen(text); i < n; i++)
    {
        if(key_char == strlen(keyword))
        {
            key_char = 0; //ensure that key_char count never goes higher than length of the keyword
        }
        if(text[i] >= start && text[i] <= finish)
        {
            if(text[i] + (keyword[key_char]-start_key) > finish)
            {
                text[i] = start + ((text[i] - start + (keyword[key_char]-start_key)) % modulo);  //handling if the key goes above the specified range
            } else {
                text[i] = text[i] + (keyword[key_char]-start_key);
            }
        }
        if(!(text[i] >= punc_start && text[i] <= punc_fin))  //skip incrementing the keyword if hit a punctuation mark or a space.
        {
            key_char = key_char + 1;
        }
    }
    return text;
}
    