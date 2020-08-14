import csv, time, datetime
from pycoingecko import CoinGeckoAPI
cg = CoinGeckoAPI()
# /usr/bin/pytthon3 /home/pi/Desktop/Crypto/getPrice.py
'''
    Phase 1: 
        create a program to run twice a day at 8am and 8pm to compare 
        to previous runs list of coins in order to be alerted of new ones.
        send a text containing new coins.
    Phase 2: [ICObuys.py]
        create an extract for the data and visualize the percent changes over time.
    Phase 3:
        run history to see how profitable coins were in the first week of ICO
        run a max price range for the coins, put $100 on each one and see what your balance would YTD.
    
'''
while True:
    
    data = cg.get_price('bitgear', vs_currencies='usd')
    # print(data)
    data 
    price_gear = float(data['bitgear']['usd'])
    price_usd = 568.441*price_gear

    body = '$'+str(price_usd)[:6]
    print(body)
    time.sleep(60)