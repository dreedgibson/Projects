#include <stdio.h>
#include <cs50.h>
#include <string.h>
#include <stdlib.h>

//function declaration
int get_key(string key);
string cipher(string text, int start, int finish, int modulo, int key);

int main(int argc, string argv[])
{
    // return an error should there be an incorrect number of arguments
    if(argc != 2)
    {
        printf("Caesar.c has one (1) command line input");
        return 1;
    }
    
    string plaintext = GetString();
    
    int k = get_key(argv[1]);
    
    int start_upper = 65; //start and end of upper case ASCII numbers
    int end_upper = 90;
    int start_lower = 97; //start and end of lower case ASCII numbers
    int end_lower = 122;
    int total_char = 26; //total number of chars
    
    string cipher_text = cipher(plaintext, start_upper, end_upper, total_char, k); //change the upper case letters
    cipher_text = cipher(cipher_text, start_lower, end_lower, total_char, k); //change the lower case letters
    
    //print the final encrypted text
    printf("%s\n", cipher_text);
    
    return 0;
    
}

//function that will take a string input and output a number for key
int get_key(string key)
{
    int k = atoi(key);
    if(k > 25)
    {
        k = k % 26;
    }
    return k;
}

//function to encode the text 
string cipher(string text, int start, int finish, int modulo, int key)
{
    for(int i = 0, n = strlen(text); i < n; i++)
    {
        if(text[i] >= start && text[i] <= finish)
        {
            if(text[i] + key > finish)
            {
                text[i] = start + ((text[i] - start + key) % modulo);  //handling if the key goes above the specified range
            } else {
                text[i] = text[i] + key;
            }
        }
    }
    return text;
}