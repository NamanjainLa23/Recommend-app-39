# Recommend-app-39
App Name Django - Poject , Module name Blog


create a virtual environment:  mkvirtualenv test

start working on virtual env: workon test  

On the root folder and run: pip install -r requirements.txt this will install all dependencies

on another command prompt window run: mongod    this will start mongo server

on virtual environment run:  python manage.py runserver    (go to the root folder first ie. inside App folder)

go to localhost on browser

use links to create new user, user profile, write blogs, update, delete, view other people blog.

open command prompt sequentially run the three python scripts: 1. webScrap_Func.py  (This will extract the data)
                                                               2. storing_scraped-data_to_mongo_desc.py    (will iterrate through each link and fetch the content)
                                                               3. nltk_module.py (will generalize the description, remove stop words, remove punctuation, remove numbers, remove extra spaces and newline character, removes special symbols, and count the occurence of each of the word).
                                                               
                                                               
Run the final python file to search your word and get the link
