import csv, twilio
from pycoingecko import CoinGeckoAPI
from twilio.rest import Client
cg = CoinGeckoAPI()
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

data = cg.get_price('bitgear', vs_currencies='usd')
# print(data)

price_gear = float(data['bitgear']['usd'])
price_usd = 568.441*price_gear

TWILIO_ACCOUNT_SID = 'AC9dbe97cd3e577cc671e8237dbd915f86'
TWILIO_AUTH_TOKEN = '9c990c745a6954c756138ec8f49727ce'

client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

drewPhone = '2145923739'
# brockPhone = '9725671997'
botPhone = '2028755446'
# patrickPhone = '2142980418'
# carPhone = '9188992204'

body = '$'+str(price_usd)[:6]

# client.messages.create(from_=botPhone, to=drewPhone, body=body)
# client.messages.create(from_=botPhone, to=brockPhone, body=body)
# client.messages.create(from_=botPhone, to=patrickPhone, body=body)
# client.messages.create(from_=botPhone, to=carPhone, body=body)