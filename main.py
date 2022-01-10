from bs4 import BeautifulSoup
from lxml import etree
import requests
import time
import socket
from pushbullet import Pushbullet
import datetime
import sys

# CONFIG START
pushbulletAPI_KEY = 'o.S1dbtZulvxmAnLJeWcJlKOfwF2N2rXNd'


microcenterItem = "https://www.microcenter.com/product/470832/Crystal_570X_RGB_ATX_Mid-Tower_Computer_Case_-_Black-Clear"
delay = True
printItem = True
# CONFIG END

try:
    pb = Pushbullet(pushbulletAPI_KEY)
except:
    print('Failed to connect to push bullet api!')

count = 0
printItemElement = False
def isConnected():
    try:
        sock = socket.create_connection(("www.speedtest.net", 80))
        if sock is not None:
            sock.close
        return True
    except OSError:
        pass
    return False


def inStockAlert():
    print('In Stock!!!!!!!!!!!!')
    push = pb.push_note('Item in stock!', 'your item is now in stock on microcenter!')

while True:
    print('checking for wifi...')
    if (isConnected() == True):
        print('Wifi connected!')
        HEADERS = ({'User-Agent':
                    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 \
                    (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36',\
                    'Accept-Language': 'en-US, en;q=0.5'})


        try:
            webpage = requests.get(microcenterItem, headers=HEADERS)
            soup = BeautifulSoup(webpage.content, "html.parser")
            dom = etree.HTML(str(soup))
        except:
            sys.exit('No wifi!')

        print('Opened webpage.')
        
        try:
            itemStatus = int(dom.xpath('/html/body/main/article/div[3]/div[1]/div[1]/div/div[2]/div[1]/p/span[2]')[0].text)
            
            if printItemElement:
                print(itemStatus)
            try:
                if (itemStatus != 0):
                    inStockAlert()
                    break
                else:
                    if printItem:
                        count += 1
                        print('Out of Stock! ' + str(count))
                    if delay:
                        time.sleep(5)
                    
            except:
                inStockAlert()
                break
                
                
        except:
            inStockAlert()

    else:
        print('No wifi...')
        time.sleep(3)
