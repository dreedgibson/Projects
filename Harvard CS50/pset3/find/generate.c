/**
 * generate.c
 *
 * Computer Science 50
 * Problem Set 3
 *
 * Generates pseudorandom numbers in [0,LIMIT), one per line.
 *
 * Usage: generate n [s]
 *
 * where n is number of pseudorandom numbers to print
 * and s is an optional seed
 */
 
#define _XOPEN_SOURCE

#include <cs50.h>
#include <stdio.h>
#include <stdlib.h>
#include <time.h>

// constant
#define LIMIT 65536

int main(int argc, string argv[])
{
    // Return a message explaining proper use of the program if an improper amount of command line arguments are input
    if (argc != 2 && argc != 3)
    {
        printf("Usage: generate n [s]\n");
        return 1;
    }

    // convert the string argv[1] to a number that will be used to generate n numbers
    int n = atoi(argv[1]);

    // If a seed is given then convert the string to a seed number, if no seed is given generate a seed for a drand
    if (argc == 3)
    {
        srand48((long int) atoi(argv[2]));
    }
    else
    {
        srand48((long int) time(NULL));
    }

    // print the random numbers generated, the LIMIT is input becuase drand only generates numbers from 0 -> 1.0
    // the numbers are multiplied by LIMIT and converted to an int so as to discard all numbers after the decimal
    for (int i = 0; i < n; i++)
    {
        printf("%i\n", (int) (drand48() * LIMIT));
    }

    // success
    return 0;
}