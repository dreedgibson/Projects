/**
 * dictionary.h
 *
 * Computer Science 50
 * Problem Set 5
 *
 * Declares a dictionary's functionality.
 */

#ifndef DICTIONARY_H
#define DICTIONARY_H

#include <stdbool.h>

// maximum length for a word
// (e.g., pneumonoultramicroscopicsilicovolcanoconiosis)
#define LENGTH 45

// I settled on 1000 rows in hash table as this would theoretically give ~14 values per row
// hopefully this results in fairly quick lookup function as the max time for lookup would be a small amount of steps
// P.S. Hopefully! (again!)
#define CAPACITY 75000

typedef struct node
{
    char word[LENGTH + 1];
    struct node* next;
} node;

// create hash table struct.
typedef struct HashTable {
    node *table[CAPACITY];
} HashTable;

int size_of_table;

/**
 * Returns true if word is in dictionary else false.
 */
bool check(char* word);

/**
 * Loads dictionary into memory.  Returns true if successful else false.
 */
bool load(char* dictionary);

/**
 * Returns number of words in dictionary if loaded else 0 if not yet loaded.
 */
unsigned int size(void);

/**
 * Unloads dictionary from memory.  Returns true if successful else false.
 */
bool unload(void);

#endif // DICTIONARY_H
