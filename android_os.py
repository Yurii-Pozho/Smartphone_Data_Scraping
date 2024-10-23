import requests
import pandas as pd
from bs4 import BeautifulSoup
from time import sleep

data = []

for p in range(1,68):
    print(p)
    url = f"https://rozetka.com.ua/ua/mobile-phones/c80003/op_system=247;page={p}/"
    r = requests.get(url)
    sleep(3)
    soup = BeautifulSoup(r.text, 'html.parser')
    
    phones = soup.findAll('div', class_="goods-tile__inner")
    
    for phone in phones:
        title = phone.find('a', class_="product-link goods-tile__heading").get('title')
        data.append(title) 
        
df = pd.DataFrame(data,columns=['Phones Title'])
df.to_csv('phones_title.csv',index=False)     
print('Everything is good')