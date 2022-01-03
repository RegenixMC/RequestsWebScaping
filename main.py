from bs4 import BeautifulSoup
from lxml import etree
import requests
import time

# CONFIG START
microcenterItem = "https://www.microcenter.com/product/470832/Crystal_570X_RGB_ATX_Mid-Tower_Computer_Case_-_Black-Clear"
delay = True
printItemElement = False
# CONFIG END


def inStockAlert():
    print('In Stock!!!!!!!!!!!!')

while True:
    HEADERS = ({'User-Agent':
                'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 \
                (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36',\
                'Accept-Language': 'en-US, en;q=0.5'})
    
    webpage = requests.get(microcenterItem, headers=HEADERS)
    soup = BeautifulSoup(webpage.content, "html.parser")
    dom = etree.HTML(str(soup))


    try:
        itemStatus = int(dom.xpath('/html/body/main/article/div[3]/div[1]/div[1]/div/div[2]/div[1]/p/span[2]')[0].text)

        if printItemElement:
            print(itemStatus)
        try:
            if (itemStatus != 0):
                inStockAlert()
                break
            else:
                if printItemElement:
                    print('Out of Stock!')
                if delay:
                    time.sleep(5)
        except:
            inStockAlert()
            break
    except:
        inStockAlert()
