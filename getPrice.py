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

data1 = cg.get_price('lgcy-network', vs_currencies='usd')
# data2 = cg.get_price('keysians-network', vs_currencies='usd')
# print(data1)

price_coin1 = float(data1['lgcy-network']['usd'])
price_usd1 = 257927.71025115204*price_coin1

# price_coin2 = float(data2['keysians-network']['usd'])
# price_usd2 = 5.22413*price_coin2

TWILIO_ACCOUNT_SID = ''
TWILIO_AUTH_TOKEN = ''

# client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

drewPhone = '2145923739'
# brockPhone = '9725671997'
botPhone = '2028755446'
# patrickPhone = '2142980418'
# carPhone = '9188992204'

body = ['LGCY $'+str(price_usd1)[:6]]
# print(body)
# client.messages.create(from_=botPhone, to=drewPhone, body=body)
# client.messages.create(from_=botPhone, to=brockPhone, body=body)
# client.messages.create(from_=botPhone, to=patrickPhone, body=body)
# client.messages.create(from_=botPhone, to=carPhone, body=body)