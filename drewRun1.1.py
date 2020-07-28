import datetime, pandas, functools
from pycoingecko import CoinGeckoAPI
cg = CoinGeckoAPI()

TICKERS = ['LINK', 'BTC', 'XLM', 'ZRX', 'ZEC', 'XTZ', 'XRP', 'REP', 'OXT', 'OMG' , 'MKR', 'LTC', 'KNC', 'ETH', 'ETC', 'EOS', 'DASH', 'DAI', 'COMP', 'BCH', 'BAT', 'ATOM']
TICKERS_low = [x.lower() for x in TICKERS]
NAMES =  cg.get_coins_list()
mapping = {
            'ticker': ['zrx', 'rep', 'bat', 'btc', 'bch', 'link',  'comp', 'atom', 'dai', 'dash', 'eos', 'eth', 'etc', 'knc', 'ltc', 'mkr', 'omg', 'oxt', 'xrp', 'xlm', 'xtz', 'zec'], 
            'name': ['0x', 'augur', 'basic-attention-token', 'bitcoin', 'bitcoin-cash', 'chainlink','compound-governance-token', 'cosmos', 'dai', 'dash', 'eos', 'ethereum', 'ethereum-classic', 'kyber-network', 'litecoin', 'maker', 'omisego', 'orchid-protocol', 'ripple', 'stellar', 'tezos', 'zcash']
            }
new_mapping = {}

dates = []
date_dummy = datetime.datetime(2013,4,27)
today = str(datetime.datetime.today().date())
while date_dummy < datetime.datetime(int(today[:4]), int(today[5:7]), int(today[8:10])):
    date_dummy = date_dummy + datetime.timedelta(days=1)
    dates.append(date_dummy)
dates_df = pandas.DataFrame({'date': dates})
dfs = [dates_df]
days = 'max'

#looping through all coins
for i in range (0,len(mapping['name'])):
    data = cg.get_coin_market_chart_by_id(mapping['name'][i], vs_currency='usd', days= days)
    coin_data = {}
    coin_dates = []
    coin_prices = []
    coin_vols = []
    coin_caps = []
    for time, val in data['prices']:
        dt = datetime.datetime.fromtimestamp(int(time)/1000)
        coin_dates.append(dt)
        coin_prices.append(val)
    for time, val in data['total_volumes']:
        coin_vols.append(val)
    for time, val in data['market_caps']:
        coin_caps.append(val)
    coin_data = {'date': coin_dates, 'prices': coin_prices, 'total_volume': coin_vols, 'market_cap': coin_caps}

    coin_dates = []
    coin_prices = []
    coin_vols = []
    coin_caps = []
    for idx, val in enumerate(coin_data['date']):
        if str(val.date()) not in coin_dates:
            coin_dates.append(str(val.date()))
            coin_prices.append(coin_data['prices'][idx])
            coin_vols.append(coin_data['total_volume'][idx])
            coin_caps.append(coin_data['market_cap'][idx])
    coin_data = pandas.DataFrame({'date': pandas.to_datetime(coin_dates), mapping['name'][i]+'_price': coin_prices, mapping['name'][i]+'_total_volume': coin_vols, mapping['name'][i]+'_market_cap':coin_caps })
    dfs.append(coin_data)


df = functools.reduce(lambda left,right: pandas.merge(left, right, on= 'date', how= 'outer'), dfs)
df.to_csv('coin_data.csv', index=False)
