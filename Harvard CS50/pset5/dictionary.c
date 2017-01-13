/**
 * dictionary.c
 *
 * Computer Science 50
 * Problem Set 5
 *
 * Implements a dictionary's functionality.
 */

#include <stdbool.h>
#include <ctype.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "dictionary.h"

// hash function declaration
unsigned long hash(char* str);

HashTable* checker;
int* table_size;

/**
 * Returns true if word is in dictionary else false.
 */
bool check(char* word)
{
    // TODO
    int i, n;
    for(i = 0, n = strlen(word); i < n; i++)
        word[i] = tolower(word[i]);
    int hash_num = hash(word);
    node* cursor = NULL;
    cursor = checker -> table[hash_num];

    
    if(checker -> table[hash_num] != NULL)
    {
        while(true)
        {
            if(strcmp(cursor -> word, word) == 0)
            {
                return true;
            } else if(cursor -> next == NULL)
            {
                break;
            } else
                cursor = cursor -> next;
        }
    return false;

    } else {
        return false;
    }
}

/**
 * Loads dictionary into memory.  Returns true if successful else false.
 */
bool load(char* dictionary)
{
    checker = realloc(checker, sizeof(HashTable));
    table_size = realloc(table_size, sizeof(int));
    size_of_table = 0;
    for(int i = 0; i < CAPACITY; i++)
    {
        checker -> table[i] = NULL;
    }
    FILE* file = fopen(dictionary, "r");
    
    while(true)
    {
        node* new_node = malloc(sizeof(node));
        if(fscanf(file, "%s", new_node -> word) == 1)
        {
            int hash_num = hash(new_node -> word);
            if(strcmp(new_node -> word, "powers") == 0)
                printf("hello");
            if(checker -> table[hash_num] == NULL)
            {
                checker -> table[hash_num] = new_node;
                new_node -> next = NULL;
            } else {
                new_node -> next = checker -> table[hash_num];
                checker -> table[hash_num] = new_node;
            }
            size_of_table++;
            *table_size = size_of_table;
        } else {
            fclose(file);
            free(new_node);
            return true;
        }
    }
    fclose(file);
    return false;
}

/**
 * Returns number of words in dictionary if loaded else 0 if not yet loaded.
 */
unsigned int size(void)
{
    if(*table_size > 0)
    {
        return *table_size;
    } else
        return 0;
}

/**
 * Unloads dictionary from memory.  Returns true if successful else false.
 */
bool unload(void)
{
    // TODO
    for(long i = 0; i < CAPACITY; i++)
    {
        node* cursor = checker -> table[i];
        while(cursor != NULL)
        {
            node* temp = cursor;
            cursor = cursor -> next;
            free(temp);
        }
        if(i == CAPACITY - 1)
        {
            free(table_size);
            free(checker);
            return true;
        }
    }

    return false;
}

/**
 * This function takes a word input and returns a hash code for the hash table
 * taken from djb2:
 * http://www.cse.yorku.ca/~oz/hash.html
 * modified to fit a hash table capacity size of CAPACITY
 */
 
unsigned long hash(char* str)
{
    unsigned long hash = 5381;
    long c;

    while ((c = (*str++)))
        hash = ((hash << 5) + hash) + c; /* hash * 33 + c */

    hash = hash % CAPACITY;
    
   return hash;
}