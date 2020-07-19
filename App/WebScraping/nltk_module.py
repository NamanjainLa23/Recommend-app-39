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
    for desc in i.values():

        desc1 = re.sub(r'\n', ' ', desc)
        final_desc = re.sub(r'[^a-zA-Z ]', '', desc1)

        word_tokens = word_tokenize(final_desc)
        filtered_sentence = [w.lower()
                             for w in word_tokens if not w in stop_words]

        total_words = word_Counter(filtered_sentence)

        for u in mycol3.find({"desc": desc}, {"_id": 0, "url": 1}):
            for url in u.values():
                print(url)
                print()
                print("===============================================================")
                print()

                x = mycol4.find_one({"url": url})
                if x:
                    print("skipped")
                    continue
                else:
                    print(desc)
                    mydict4 = {"url": url, "desc": final_desc,
                               "counter": total_words}
                    x = mycol4.insert_one(mydict4)

        # print(final_desc)    #description in paragraph
        # print(filtered_sentence)   # description words in a list
        # print(total_words)   # word counter
