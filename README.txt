IR Project 2023
Subject- IR
Date- 10/12/23
Project Name- Tourism Related Search


About the Project
This project is a tourism-related search information retrieval system designed to provide users with relevant information about tourist destinations, attractions, services and hotels.Also this project provides facility to mark the resultant searches as relevant or non relevant documents by user.

Features:
1. Stemming, Stopwords removal, Tokenisation of document has implemented and coded in preprocess.py.
2. Building the inverted index, and tfidf weighting done in main.py it is important part to map the document with its words to reduce seraching time.
3. Calculating the cosine similarity and ranking the documents done in Result.py.
4. Writing the result into "/dist/Results.txt"
5. Capturing user feedback
6. Integrating the IR system in flask.


Prerequisites:
- Python latest version/ any python plateform (juputer/collab)
- data_rate_limit should greater than 100000000, to run project 
  * if using jupyter use- jupyter notebook --NotebookApp.iopub_data_rate_limit=1.0e10
- nltk libaries installed (all of these can be downloaded using python3 -> import nltk -> nltk.download('corpus | tokenize | stem.porter'))
- Pip
- Virtualenv


Run The PRoject-
- open python plateform 
(if using jupyter use-
1. jupyter notebook --NotebookApp.iopub_data_rate_limit=1.0e10 
2. python -Xfrozen_modules=off server.ipynb (in source code) anaconda terminal )
-Open Server.ipynb file (in jupyter or server.py) run code (take time for building inverted indexing)
-go to the link provided by flask
-run the server and get result


Dataset-
-Inside assets namely "tourist_data.txt"
-Github link of dataset- https://github.com/Akashsnar/IR-Tourism-data

Team Details:
Akash Singh Narvariya S20210010012
Pranav Singh S20210010180
