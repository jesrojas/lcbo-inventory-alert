import os
import sys
import json
import requests
from pymongo import MongoClient
from bs4 import BeautifulSoup


# # Prototype variable, ideally we should have this as a user input. But we are doing a demostration
pageUrl = "https://www.lcbo.com/webapp/wcs/stores/servlet/en/lcbo/baileys-colada-19418"
# # User Agent is used as a way for the website to verify that the request is being requested
# # from a browser
user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36"

# Inventory request will timeout after 4 seconds
product_data_request = requests.get(
    pageUrl, timeout=4, headers={'User-Agent': user_agent})
product_content = product_data_request.content

html_data = BeautifulSoup(product_content, 'html.parser')
title = {}
title['text'] = html_data.title.text

string_db = os.environ.get('MONGO_URL')
db = MongoClient(string_db).db.inventory
print(db)
try:
    db.insert_one(title)
    print(f'inserted {title}')
except:
    print(sys.exc_info())
