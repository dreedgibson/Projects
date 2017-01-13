/**
 * helpers.c
 *
 * Computer Science 50
 * Problem Set 3
 *
 * Helper functions for Problem Set 3.
 */
       
#include <cs50.h>
#include <stdio.h>
#include "helpers.h"

/**
 * Returns true if value is in array of n values, else false.
 */
bool search(int value, int values[], int n)
{
    if(n < 0)
    {
        return false; //can not search a negative set
    }
    //define a start and middle int for use in the do loop
    int middle;
    int start = 0;
    
    do 
    {
        middle = (n + start) / 2; //calc middle
        if(value == values[middle])
        {
            return true; //found the number
        }
        if(value < values[middle])
        {
            n = n - 1; //throw away the half of numbers that are greater than middle
        } else {
            start = middle + 1; //throw away half of numbers that are less than middle
        }
    } while(start <= n); //break out of loop and return false if start every becomes greater than n
    
    return false;
}

/**
 * Sorts array of n values.
 */
void sort(int values[], int n)
{
    int swap_count;
    
    do
    {
        swap_count = 0; //need swap count for bubble sort 
        
        for(int i = 0; i < n; i++)
        {
            if(values[i] > values[i+1])
            {
                int temp = values[i];  //store the bubbled number temporarily
                values[i] = values[i+1];
                values[i+1] = temp; //make swap and increment swap count
                swap_count = swap_count + 1;
            }
        }
    } while(swap_count > 0); //exit loop only when swap count == 0
    return;
}