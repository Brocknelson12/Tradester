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

# if len(results) > 1 or len(near) > 4:

TWILIO_ACCOUNT_SID = 'AC9dbe97cd3e577cc671e8237dbd915f86'
TWILIO_AUTH_TOKEN = '0265f8d1c3bffaa4312e577615c9924f'

client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

drewPhone = '2145923739'
# brockPhone = '9725671997'
botPhone = '2028755446'
# patrickPhone = '2142980418'
# carPhone = '9188992204'

body = str(new)
client.messages.create(from_=botPhone, to=drewPhone, body=body)
# client.messages.create(from_=botPhone, to=brockPhone, body=body)
# client.messages.create(from_=botPhone, to=patrickPhone, body=body)
# client.messages.create(from_=botPhone, to=carPhone, body=body)