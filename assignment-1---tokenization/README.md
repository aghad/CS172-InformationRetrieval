# CS172 - Assignment 1 (Tokenization)

### Team member 1 - Kevin Ni

### Team member 2 - Aden Ghadimi

## How to use
We developed this in python, and you must the download packages for installing NLTK. 

Here are the instructions. 

Installing NLTK on Windows 10

Step 1: Check Python Version.

> $python --version

Step 2: Install Numpy

> $pip install numpy

Step 3: Install NLTK

> $pip install nltk

Step 4: Check if NLTK is installed 

"$python import nltk"

Afterwards, Clone Repository, and run on either command prompt or the IDE of your choosing.

Make sure to have python version 3 installed. This can be found [here](https://www.python.org/download/releases/3.0/)

Make sure to have the nltk package installed. This can be found [here](https://www.nltk.org/install.html)

Run `py read_index.py` to pull up a help GUI of possible commmands.

Possible flags are:
> --doc

> --term

> --write

## Implementation
### Made 3 classes
Posting_Node stores positions and frequencies for a given document ID. This is used by Term_Node

Term_Node stores number of documents the term has appeared in, occurrences, and a hashmap of Posting_Node's for a given term ID.

Doc_Node stores number of distinct terms and number of total terms for a given document ID.

### Made a few global variables
term_Index is a hashmap that maps terms to term IDs

doc_Index is a hashamp that maps document names to doc IDs

term_Info is a hashmap that maps term IDs to Term_Node's

stop_words is a hashset of words

## Assignment Parts
### Part 1
Check repeated documents 

New document ID

Check to be deleted

Lowercase the words

Remove underscores

Process the text string

For each token match

Remove apostrophe

Remove stop-words

Stemming

Add the token to our list.

### Part 2
Create tokens

Match the unique term within the ID, and if the token is not in the term_index, then you would add

Set up the term_info

Add the to term_info

Add distinct terms to doc_Index

Add total words to doc_Index

### Part 3
The file read_index.py uses argparse library to help with the command parsing

Should the `--write` flag be found, enable writing to disk

Should either the `--term` or `--doc` flag be found, run process_commands()

### Part Extra Credit
Within function write_to_disk()

Build term_index.txt

Save a byte_counter and offset, loop through each term_node in term_Index

Loop through each posting_node in the posting_list from term_node

Loop through each position in posting_node's list

Build term_info.txt

While in the term loop, write to file with the offset saved

Build docids.txt

Build termidis.txt

## Completion
We attempted all parts of the extra credit, including stemming.
