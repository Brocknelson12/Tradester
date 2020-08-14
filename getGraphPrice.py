import time, datetime
from pycoingecko import CoinGeckoAPI
cg = CoinGeckoAPI()
import plotly.graph_objects as go

while True:
    data = cg.get_price('bitgear', vs_currencies='usd')
    stamp = str(datetime.datetime.now())[:22]
    price = '$'+str(568.441*float(data['bitgear']['usd']))[:6]
    print([stamp, price])
    time.sleep(5)