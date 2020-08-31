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
btc_price = float(cg.get_price('bitcoin', vs_currencies='usd')['bitcoin']['usd'])
btc_wallet_coinbase = 0.04883647*btc_price
btc_wallet_csahapp = 0.00846508*btc_price
btc_wallet = str('BTC $'+str(btc_wallet_coinbase+btc_wallet_csahapp)[:6])

link_price = float(cg.get_price('chainlink', vs_currencies='usd')['chainlink']['usd'])
link_wallet = str('LINK $'+str(11.34571318*link_price)[:6])


alt_wallet = []
dot_price = float(cg.get_price('polkadot', vs_currencies='usd')['polkadot']['usd'])
dot_wallet = str('DOT $'+str(16.00395043*dot_price)[:6])
om_price = float(cg.get_price('mantra-dao', vs_currencies='usd')['mantra-dao']['usd'])
om_wallet = str('OM $'+str(125.335*om_price)[:6])
stake_price = float(cg.get_price('xdai-stake', vs_currencies='usd')['xdai-stake']['usd'])
stake_wallet = str('STAKE $'+str(1.096*stake_price)[:6])
alt_wallet = 'ALTs $'+str(float(16.00395043*dot_price)+float(125.335*om_price)+float(1.096*stake_price))[:6]

TWILIO_ACCOUNT_SID = ''
TWILIO_AUTH_TOKEN = ''

# client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

drewPhone = '2145923739'
# brockPhone = '9725671997'
botPhone = '2028755446'
# patrickPhone = '2142980418'
# carPhone = '9188992204'

body = str(btc_wallet+'\n'+link_wallet+'\n'+alt_wallet+'\n'+dot_wallet+'\n'+om_wallet+'\n'+stake_wallet)
print(body)
# client.messages.create(from_=botPhone, to=drewPhone, body=body)
# client.messages.create(from_=botPhone, to=brockPhone, body=body)
# client.messages.create(from_=botPhone, to=patrickPhone, body=body)
# client.messages.create(from_=botPhone, to=carPhone, body=body)