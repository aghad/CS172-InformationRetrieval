import re
import os
import zipfile

# Regular expressions to extract data from the corpus
doc_regex = re.compile("<DOC>.*?</DOC>", re.DOTALL)
docno_regex = re.compile("<DOCNO>.*?</DOCNO>")
text_regex = re.compile("<TEXT>.*?</TEXT>", re.DOTALL)
token_regex = re.compile(r"\w+")


with zipfile.ZipFile("ap89_collection_small.zip", 'r') as zip_ref:
    zip_ref.extractall()
   

#Initialize all the global variables
docID = 1
termID = 1  
termIndex = dict()
docIndex = dict()

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

            # step 1 - lower-case words, remove punctuation, remove stop-words, etc. 
            
            ## lowercase the word
            text = text.lower();

            ## Process  the text string
            if(docID <= 1):
                print(docno, ":");

                tokens = re.findall(token_regex, text)
                
                # print(tokens)
                # if token:
                    # print(tokens)
                # else:
                    # print("No match")
                    
                # for token in tokens:
            
            # step 2 - create tokens 
            
            ## New Document ID
                docIndex[docno] = docID
                docID = docID + 1
                print(docIndex[docno])
                
                pos = 1
                for token in tokens:
                    if not token in termIndex:
                        termIndex[token] = termID
                        termID = termID + 1
                    print("(", termIndex[token], ", ", docIndex[docno], ", ", pos, ") ")
                    pos = pos + 1
                    
            
            # step 3 - build index
            
            
            
            