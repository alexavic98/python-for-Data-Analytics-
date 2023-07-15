import requests
from bs4 import BeautifulSoup


url = "https://www.jumia.com.ng/catalog/?q=iphones"
response = requests.get(url)
response = response.content
phones = []
soup = BeautifulSoup(response, "html.parser")
div = soup.find("div", class_="-paxs row _no-g _4cl-3cm-shs" )
articles = div.find_all("article", class_="prd _fb col c-prd")
for article in articles:
    items = article.find("div", class_ = "info")
    names = items.find("h3", class_= "name").text
    # text was added to return only the text in that tag. i.e getting rid of all other unwanted elements
    #print(names)
    price = items.find("div",class_="prc").text
    price = price[1:]
    # this line ((price = price[1:])) was added to return the values from the first index and above. i.e leaving out the 0 index
    price = price[1:]
    # this line ((price = float(price[1:])) can be added to convert the priv=ce from a str to a float
    #print(names)
    items_old_price = article.find("div", class_="s-prc-w")
    old_price = items_old_price.find("div", class_="old").text
    old_price = old_price[1:]
    #print(old_price)
    #lets create a list that contains the phone name, price and old price
   
    phones.append([names, price, old_price])
    print(phones)
import pandas as pd
pd.DataFrame(phones, columns=["names", "price", "old_price"])

phones.to_csv("jumia phones.csv")
    
