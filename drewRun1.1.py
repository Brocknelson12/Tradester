import datetime, pandas
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

all_coins = pandas.DataFrame()
coin_data = pandas.DataFrame()
timestamps = pandas.date_range(start='2013-04-27',end= str(datetime.datetime.today())[:10])
coin_data['timestamps'] = timestamps
all_coins['timestamps'] = timestamps
days = 'max'
x=0
# print(str(datetime.datetime.today())[:10])

coins = []
df = pandas.DataFrame()
#looping through all coins
for i in range (0,len(mapping['name'])):
    coin_tkr = mapping['ticker'][i]
    data = cg.get_coin_market_chart_by_id(mapping['name'][i], vs_currency='usd', days= days)
    
        # print(data)
    coin_times = []
    coin_prices = []
    #price is only variable we are using
    #need to get a list of pandas timestamps to join list on
    for entry in data['prices']:
        time = entry[0]
        # new_time = pandas.to_datetime(time)
        # coin_times.append(str(datetime.datetime.fromtimestamp(int(time)/1000).date()))
        coin_times.append(entry[0])
        coin_prices.append(entry[1])
    # print(df)
    if 'timestamps' in df: 
        df = df.merge(pandas.DataFrame({"prices_"+mapping['name'][i]:coin_prices, "timestamps": coin_times}), on="timestamps",how="left")
    else:
        df = pandas.DataFrame({"timestamps": coin_times, "prices_"+mapping['name'][i]:coin_prices})
        print(df)


#  df.to_csv()   
stamps = []
for time in df['timestamps']:
    new_time = str(datetime.datetime.fromtimestamp(int(time)/1000).date())
    stamps.append(new_time)
df['timestamps'] = stamps
# df['timestamps']
df.to_csv('coin_data.csv', index=False)