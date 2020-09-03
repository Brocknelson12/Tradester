import csv, twilio, requests
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
btc_price = float(cg.get_price('bitcoin', vs_currencies='usd')['bitcoin']['usd'])
trending = requests.get('https://api.coingecko.com/api/v3/search/trending').json()['coins']
# print(trending)
trends = []
for i in trending:
    trends.append(str(i['item']['symbol']+'-'+str(i['item']['market_cap_rank'])))
print(trends)
TWILIO_ACCOUNT_SID = ''
TWILIO_AUTH_TOKEN = ''

# client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

drewPhone = '2145923739'
# brockPhone = '9725671997'
botPhone = '2028755446'
# patrickPhone = '2142980418'
# carPhone = '9188992204'

body = str(trends)
print(body)
# client.messages.create(from_=botPhone, to=drewPhone, body=body)
# client.messages.create(from_=botPhone, to=brockPhone, body=body)
# client.messages.create(from_=botPhone, to=patrickPhone, body=body)
# client.messages.create(from_=botPhone, to=carPhone, body=body)