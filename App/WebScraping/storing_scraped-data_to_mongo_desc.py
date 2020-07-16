from bs4 import BeautifulSoup
import requests
import re
from pymongo import MongoClient

democlient = MongoClient()
myclient = MongoClient('localhost', 27017)
mydb = myclient["Intern"]
mycol1 = mydb["Scrap1"]
mycol2 = mydb["Scrap2"]
mycol3 = mydb["Scrap3"]

desc_link = list(mycol1.find({}, {"_id": 0, "url": 1}))
for link in desc_link:
    for k in link.values():
        desc = ""
        try:
            source = requests.get(k).text
            soup = BeautifulSoup(source, 'lxml')

            for p in soup.find_all('p'):
                desc = desc + " " + p.text

        except:
            print("Network Error")

        if desc:
            pass
        else:
            desc = "No Description in given page"
            pass

        x = mycol3.find_one({"url": k})
        if x:
            print("skipped")
            continue
        else:
            print(desc)
            mydict3 = {"url": k, "desc": desc}
            x = mycol3.insert_one(mydict3)
