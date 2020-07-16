from bs4 import BeautifulSoup
import requests
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import re
from pymongo import MongoClient

democlient = MongoClient()
myclient = MongoClient('localhost', 27017)
mydb = myclient["Intern"]
mycol1 = mydb["Scrap1"]
mycol2 = mydb["Scrap2"]
mycol3 = mydb["Scrap3"]
mycol4 = mydb["Scrap4"]


def word_Counter(s):
    count1 = {}
    for char in s:
        count1[char] = s.count(char)
    return count1


stop_words = set(stopwords.words('english'))

for i in mycol3.find({}, {"_id": 0, "desc": 1}):

    # i = mycol3.find_one(
    #    {"url": "https://www.coindesk.com/hackers-take-over-prominent-crypto-twitter-accounts-in-simultaneous-attack"}, {"_id": 0, "desc": 1})

    for desc in i.values():
        desc1 = re.sub(r'\n', ' ', desc)
        #desc2 = re.sub(r'\s+', ' ', desc1)
        #desc2 = re.sub(r'â', "'", desc1)
        #desc3 = re.sub(r'â', "'", desc2)
        #desc4 = re.sub(r'â¢', ".", desc3)
        #desc5 = re.sub(r'\[[0-9]*\]', '', desc4)
        final_desc = re.sub(r'[^a-zA-Z ]', '', desc1)

        word_tokens = word_tokenize(final_desc)
        filtered_sentence = [w.lower()
                             for w in word_tokens if not w in stop_words]

        total_words = word_Counter(filtered_sentence)

        print(filtered_sentence)
        print(total_words)
        print()
        print("===============================================================")
        print()
