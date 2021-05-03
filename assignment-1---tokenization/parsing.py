from nltk.stem import PorterStemmer
# Make sure to run "pip install nltk"

import re
import os
import zipfile

# Regular expressions to extract data from the corpus
doc_regex = re.compile("<DOC>.*?</DOC>", re.DOTALL)
docno_regex = re.compile("<DOCNO>.*?</DOCNO>")
text_regex = re.compile("<TEXT>.*?</TEXT>", re.DOTALL)
token_regex = re.compile(r"\w+(\.?\'?\,?\w+)*")

# Initialize all the global variables
doc_ID_counter = 1
term_ID_counter = 1

# A hashmap of term -> ID
term_Index = dict()
# A hashmap of doc -> ID
doc_Index = dict()
# A hashmap of term -> term_node
term_Info = dict()

stop_words = set()
stemmer = PorterStemmer()

# Initialize classes
class Posting_Node:
    def __init__(self, ID):
        self.ID = ID
        self.positions = []
        
    def add_Position(self, position):
        self.positions.append(position)
        
    def get_ID(self):
        return self.ID
    
    def get_Frequency(self):
        return len(self.positions)
        
    def get_Positions(self):
        return self.positions
        
class Term_Node:
    def __init__(self, ID):
        self.ID = ID
        
        # A hashmap of docID -> Posting_Node
        self.posting_list = dict()
        
    def add_Position(self, docID, position):
        if docID not in self.posting_list:
            self.posting_list[docID] = Posting_Node(docID)
        self.posting_list[docID].add_Position(position)
    
    def get_ID(self):
        return self.ID
    
    def get_Documents(self):
        return len(self.posting_list)
    
    def get_Occurrences(self):
        occurrences = 0
        for key in self.posting_list:
            occurrences = occurrences + self.posting_list[key].get_Frequency()
        return occurrences
    
    def get_Posting_List(self):
        return self.posting_list
        
    def get_Posting_Node(self, docID):
        return self.posting_list[docID]

# Initialize stop_words
stop_file = open("stopwords.txt","r")
for line in stop_file:
    line = line.strip("\n")
    stop_words.add(line)
stop_file.close()

# Retrieve the names of all files to be indexed in folder ./ap89_collection_small of the current directory
for dir_path, dir_names, file_names in os.walk("ap89_collection_small"):
    allfiles = [os.path.join(dir_path, filename).replace("\\", "/") for filename in file_names if (filename != "readme" and filename != ".DS_Store")]
    
for file in allfiles:
    with open(file, 'r', encoding='ISO-8859-1') as f:
        filedata = f.read()
        result = re.findall(doc_regex, filedata)  # Match the <DOC> tags and fetch documents

        for document in result[0:]:
            # Retrieve contents of DOCNO tag
            docno = re.findall(docno_regex, document)[0].replace("<DOCNO>", "").replace("</DOCNO>", "").strip()
            # Retrieve contents of TEXT tag
            text = "".join(re.findall(text_regex, document))\
                      .replace("<TEXT>", "").replace("</TEXT>", "")\
                      .replace("\n", " ")

            # Part 1 - lower-case words, remove punctuation, remove stop-words, etc. 
            tokens = []
            
            ## Checking repeated documents
            if docno in doc_Index:
                continue
                
            ## New Document ID
            doc_Index[docno] = doc_ID_counter
            doc_ID_counter = doc_ID_counter + 1
            
            ## CHECK TO BE DELETED
            # if (doc_Index[docno] >= 2):
                # continue
            
            
            ## Lowercase the word
            text = text.lower();
            
            ## Remove underscores (\w allows underscores for some reason)
            text = text.replace("_","")

            ## Process  the text string
            print(docno, ":");

            for match in re.finditer(token_regex, text):
                token = (match.group())
                
                # Remove apostrophe
                token = token.split("'")[0]
                
                # Remove stop-words
                if (token in stop_words):
                    continue
                
                # Stemming
                token = stemmer.stem(token)
                
                # Add the token to our list
                tokens.append(token)
            
            # Part 2 - create tokens
            pos_counter = 1
            
            for token in tokens:
                
            ## Matching unique term ID
                if token not in term_Index:
                    term_Index[token] = term_ID_counter
                    term_ID_counter = term_ID_counter + 1
                
                # print("(", term_Index[token], ", ", token, ", ", doc_Index[docno], ", ", pos_counter, ") ") 
                
                ## Setting up term_Info
                if term_Index[token] not in term_Info:
                    term_Info[term_Index[token]] = Term_Node(term_Index[token])
                
                ### Add this position
                # print(token, " ", term_Index[token], " ", pos_counter)
                term_Info[term_Index[token]].add_Position(doc_Index[docno], pos_counter)
                
                pos_counter = pos_counter + 1
                
# Part Extra Credit

## Building term_index.txt
byte_counter = 0
offset = 0

term_Index_file = open("term_index.txt","w")
term_Info_file = open("term_info.txt","w")

for term_name in term_Index:
    offset = byte_counter
    
    term_Index_file.write(str(term_Index[term_name]))
    byte_counter = byte_counter + len(str(term_Index[term_name]))
    
    for posting_node_key in term_Info[term_Index[term_name]].get_Posting_List():
        posting_node = term_Info[term_Index[term_name]].get_Posting_List()[posting_node_key]
        for position in posting_node.get_Positions():
        
            term_Index_file.write("\t" + str(posting_node.get_ID()) + ":" + str(position))
            byte_counter = byte_counter + len(str(posting_node.get_ID())) + len(str(position)) + 2
            
    term_Index_file.write("\n")
    byte_counter = byte_counter + 2
    
    ## Building term_info.txt
    term_Info_file.write(str(term_Index[term_name]) + "\t" + str(offset) + "\t" + str(term_Info[term_Index[term_name]].get_Occurrences()) + "\t" + str(term_Info[term_Index[term_name]].get_Documents()) + "\n")

term_Index_file.close()
term_Info_file.close()

## Building term_info.txt
# readding = open("term_index.txt","r")
# readding.seek(14)
# print(readding.readline())

## Building docids.txt
docids_file = open("docids.txt","w")
for doc_name in doc_Index:
    docids_file.write(str(doc_Index[doc_name]) + "\t" + str(doc_name) + "\n")
docids_file.close()

## Building termidis.txt
termids_file = open("termids.txt","w")
for term_name in term_Index:
    termids_file.write(str(term_Index[term_name]) + "\t" + str(term_name) + "\n")
termids_file.close()

def process_commands(**kwargs):
    print("hi")
    

