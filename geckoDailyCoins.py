import csv, twilio
from pycoingecko import CoinGeckoAPI
from twilio.rest import Client
cg = CoinGeckoAPI()
'''
    Phase 1: 
        create a program to run twice a day at 8am and 8pm to compare 
        to previous runs list of coins in order to be alerted of new ones.
        send a text containing new coins.
    Phase 2:
        create an extract for the data and visualize the percent changes over time.
    Phase 3:
        run history to see how profitable coins were in the first week of ICO
        run a max price range for the coins, put $100 on each one and see what your balance would YTD. 
    
'''
# old = list()
with open('geckoCoinsList.csv', 'r') as inFile:
    old = list(csv.reader(inFile))
    old = old[0]


current = list()
data = cg.get_coins_list()
for i in data:
    current.append(i['id'])

new = list()
for i in current:
    if i not in old:
        new.append(i)

with open('geckoCoinsList.csv', 'w') as outFile:
    writer = csv.writer(outFile)
    writer.writerow(current)

print(new)