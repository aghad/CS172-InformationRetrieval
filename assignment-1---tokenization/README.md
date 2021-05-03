# CS172 - Assignment 1 (Tokenization)

## Team member 1 - Kevin Ni
## Team member 2 - Aden Ghadimi


#Provide a short explanation of your design.

Exrtacted all the data from the corpus of the regular expressions. 
Developed a hashmap to store the values and i.d's.
While we're iterating through the corpus.

Initalized the stop.words, and retrieved the names of all files to be indexed within the folder ./ap89_collection_small of the current directory.
As we traverse through the files, we retrieve the contents of the DOCNO tag, then the TEXT tag.

Part1: Check repeated documents 
New document ID
Check to be deleted
Lowercase the words
Process the text string
Traverse throughout, while removing apostrophe ****?****
Remove stop-words
Stemming
Add the token to our list.
Building term_docids.txt 
Building termidis.txt
Process the text string



Part2: Create tokens
Match the unique term within the ID, and if the token is not in the term_index, then you would add to the counter.
Set up the term information
Add the position of the counter
Add the total words



#Extra Credit
Open the index file up, and traverse 
Check if a query is valid. 



#Regualr expressions to extract data from the corpus

#Hashmap of terms -> ID
#Hashmaps of documents -> ID
#Hashmaps of terms -> term_node

#Initalize classes



We developed this in python, and you must the download packages for installing NLTK. 
Here are the instructions. 
Installing NLTK on Windows 10
Step 1:Check Python Version.
"$python --version"
Step 2: Install Numpy
"$pip install numpy"
Step 3: Install NLTK
"$pip install nltk"
Step 4: Check if NLTK is installed 
"$python import nltk"
Afterwards, Clone Repository, and run on either command prompt or the IDE of your choosing. 

#if you attempted the extra credit (stemming), etc. 
