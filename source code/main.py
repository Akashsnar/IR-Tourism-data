from preprocess import importQuery, importTweets, buildIndex, lengthOfDocument, tweetdict, returnDocs
from results import retrieve
from write import resultFileCreation
import nltk


nltk.download('stopwords')


nltk.download('punkt')



nltk.download('punkt_tab')


def once(tweets):
    print("\n Stemming,tokenisation and removal of stop words \n")
    
    print("\n Building the inverted index \n")
    verbose = True

    index = buildIndex(tweets, verbose)

    print("\n  Done! \n");
    return index;


def evaluate(index, tweets, document_length, query=""):
    print(query)

    print("\n Stemming,tokenisation and removal of stop words \n")


    query_file = importQuery(query)

#     print("\n Preprocessing Done! \n")

#     print("\n Building the inverted index \n")


#     print("\n Retrieving and Ranking..\n")


    ranking = retrieve(query_file, index, document_length)

    print("\n Retrieval and Ranking Done! \n")

    print("\n Writing Result File... \n")

    resultFileCreation(ranking)

    print("\n Result File Creation Done! \n")


if __name__ == "__main__":
    evaluate()
