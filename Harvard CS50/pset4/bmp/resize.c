/**
 * copy.c
 *
 * Computer Science 50
 * Problem Set 4
 *
 * Copies a BMP piece by piece, just because.
 */
       
#include <stdio.h>
#include <stdlib.h>

#include "bmp.h"

int main(int argc, char* argv[])
{
    // ensure proper usage
    if (argc != 4)
    {
        printf("Usage: ./resize n infile outfile\n");
        return 1;
    }

    // get the value n for resizing
    char* n = argv[1];
    int m = atoi(n);
    
    // ensure n is greater than or equal to one
    if(m < 1)
    {
        printf("n must be greater than or equal to 1");
        return 2;
    }
    
    // remember filenames
    char* infile = argv[2];
    char* outfile = argv[3];

    // open input file 
    FILE* inptr = fopen(infile, "r");
    if (inptr == NULL)
    {
        printf("Could not open %s.\n", infile);
        return 3;
    }

    // open output file
    FILE* outptr = fopen(outfile, "w");
    if (outptr == NULL)
    {
        fclose(inptr);
        fprintf(stderr, "Could not create %s.\n", outfile);
        return 4;
    }

    // read infile's BITMAPFILEHEADER
    BITMAPFILEHEADER bf;
    fread(&bf, sizeof(BITMAPFILEHEADER), 1, inptr);

    // read infile's BITMAPINFOHEADER
    BITMAPINFOHEADER bi;
    fread(&bi, sizeof(BITMAPINFOHEADER), 1, inptr);

    // declare outfile's BITMAPFILEHEADER
    BITMAPFILEHEADER bfout = bf;
    
    // declare outfile's BITMAPINFOHEADER
    BITMAPINFOHEADER biout = bi;

    // ensure infile is (likely) a 24-bit uncompressed BMP 4.0
    if (bf.bfType != 0x4d42 || bf.bfOffBits != 54 || bi.biSize != 40 || 
        bi.biBitCount != 24 || bi.biCompression != 0)
    {
        fclose(outptr);
        fclose(inptr);
        fprintf(stderr, "Unsupported file format.\n");
        return 4;
    }

    // resize image by the factor of n
    if(m > 1)
    {
        biout.biHeight = m * bi.biHeight;
        biout.biWidth = m * bi.biWidth;
    }

    // determine padding for scanlines
    int padding =  (4 - (bi.biWidth * sizeof(RGBTRIPLE)) % 4) % 4;
    int padding_out = (4 - (biout.biWidth * sizeof(RGBTRIPLE)) % 4) % 4;

    if(m > 1)
    {
        biout.biSizeImage = ((biout.biWidth) * abs(biout.biHeight) * sizeof(RGBTRIPLE)) + m * padding_out;
        bfout.bfSize = biout.biSizeImage + 54;
    }

    // write outfile's BITMAPFILEHEADER
    fwrite(&bfout, sizeof(BITMAPFILEHEADER), 1, outptr);

    // write outfile's BITMAPINFOHEADER
    fwrite(&biout, sizeof(BITMAPINFOHEADER), 1, outptr);

    // iterate over infile's scanlines
    for (int i = 0, biHeight = abs(bi.biHeight); i < biHeight; i++)
    {
        for (int l = 1; l <= m; l++)
        {
            // iterate over pixels in scanline
            for (int j = 0; j < bi.biWidth; j++)
            {
                // temporary storage
                RGBTRIPLE triple;
                
                // read RGB triple from infile
                fread(&triple, sizeof(RGBTRIPLE), 1, inptr);
                
                for (int o = 1; o <= m; o++)
                {
                    // write RGB triple to outfile
                    fwrite(&triple, sizeof(RGBTRIPLE), 1, outptr);
                }
            }
            // skip over padding, if any
            fseek(inptr, padding, SEEK_CUR);
    
            // then add it back (to demonstrate how)
            for (int k = 0; k < padding_out; k++)
            {
                fputc(0x00, outptr);
            }
            
            // move cursor back to beginning of row
            if(l != m)
                fseek(inptr, -bi.biWidth * 3 - padding, SEEK_CUR);
        }
    }

    // close infile
    fclose(inptr);

    // close outfile
    fclose(outptr);

    // that's all folks
    return 0;
}
