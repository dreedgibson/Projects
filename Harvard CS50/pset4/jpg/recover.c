/**
 * recover.c
 *
 * Computer Science 50
 * Problem Set 4
 *
 * Recovers JPEGs from a forensic image.
 */

#include <stdio.h>
#include <stdint.h>
#include <cs50.h>

typedef uint8_t  BYTE;

bool jpgcheck(BYTE buffer[]);

int main(void)
{
    // Store card.raw
    char* jpgfile = "card.raw";
    
    // open input file
    FILE* jpg = fopen(jpgfile, "r");
    if(jpg == NULL)
    {
        printf("could not open %s", jpgfile);
        return 1;
    }
    
    // declare the buffer variable
    BYTE buffer[512];
    
    int jpgnum = 0;
    FILE* img = NULL;
    
    // read the file until it reaches the end of the card
    do 
    {
        char title[8]; //create the title of the jpeg
        while(jpgcheck(buffer))
        {
            if(jpgnum < 10)
            {
                sprintf(title, "00%i.jpg", jpgnum); //need two zeros if the number is less than 10 and 1 if 10 or greater
                img = fopen(title, "w");
            } else
            {
                sprintf(title, "0%i.jpg", jpgnum);
                img = fopen(title, "w");
            }
            if(img == NULL)
            {
                printf("could not open %s for writing", title);
                return 2;
            }
            fwrite(&buffer, sizeof(BYTE), 512, img); //write the first 512 byte block 
            
            fread(&buffer, sizeof(BYTE), 512, jpg); //read in the next 512 byte block
            while(!jpgcheck(buffer))
            {
                // while we have not come across another jpg signature continue to write 512 byte blocks 
                fwrite(&buffer, sizeof(BYTE), 512, img);
                
                // if we hit end of file break out of loop
                if(fread(&buffer, sizeof(BYTE), 512, jpg) == 0)
                {
                    break;
                }
            }
            fclose(img); //close the current img
            jpgnum++;
        }
        
    } while(fread(&buffer, sizeof(BYTE), 512, jpg) != 0);
   
    fclose(jpg);
    return 0;
}

bool jpgcheck(BYTE buffer[])
{
    if((buffer[0] == 0xff && buffer[1] == 0xd8 && buffer[2] == 0xff && buffer[3] == 0xe0) || 
        (buffer[0] == 0xff && buffer[1] == 0xd8 && buffer[2] == 0xff && buffer[3] == 0xe1))
        {
            return true;
        } else
        {
            return false;
        }
}