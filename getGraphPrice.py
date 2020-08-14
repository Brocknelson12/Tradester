import time, datetime
from pycoingecko import CoinGeckoAPI
cg = CoinGeckoAPI()
import plotly.graph_objects as go

while True:
    data = cg.get_price('bitgear', vs_currencies='usd')
    curr_price = cg.get_coin_market_chart_by_id('bitgear', vs_currency='usd', days='max')
    stamp = str(datetime.datetime.fromtimestamp(int(curr_price['prices'][0][0])/1000))
    price = str(curr_price['prices'][0][1])[:6]
    wallet = '$'+str(568.441*float(curr_price['prices'][0][1]))[:6]

    print([stamp, price, wallet])
    time.sleep(60)