from flask import Flask
from flask import render_template
from flask import request
import main
import json
from preprocess import importTweets,lengthOfDocument, returnDocs, tweetdict
app = Flask(__name__)


# datas = importTweets()
# index=main.once(datas)
# document_length=lengthOfDocument(index, datas)


with open("datas.json") as f:
    datas = json.load(f)
with open("index.json") as f:
    index = json.load(f)
with open("document_length.json") as f:
    document_length = json.load(f)


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/display-results", methods=["GET"])
def hello_world():
    query = request.args.get('query', '')
    print(request)
    main.evaluate(index, datas, document_length, query)
    print("query stop word removal preproccesed and retervied");  
    tweetsMap = tweetdict()
    print("table formed with the keys and data");
    scoreMap = returnDocs()
    print("return result for search document");
    KrelevantDocs = dict(list(scoreMap.items())[1:11])
    print("he2");
    
    
    KrelevantDocs = dict(list(scoreMap.items())[1:11])
    # print(KrelevantDocs)
    finList = []
    k = 0
    for key, val in KrelevantDocs.items():
        mylist = []
        k += 1
        mylist.append(k)
        mylist.append(tweetsMap[key])
        mylist.append(val)
        mylist.append(key)
        finList.append(mylist)
    print(finList)

    return render_template("displayTable.html", tweet_list=finList)


app.run()
