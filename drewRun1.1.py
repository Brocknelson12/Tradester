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

# all_coins = pandas.DataFrame()
# coin_data = pandas.DataFrame()
# timestamps = pandas.date_range(start='2013-04-27',end= str(datetime.datetime.today())[:10])
# coin_data['timestamps'] = timestamps
dates = []
date_dummy = datetime.datetime(2013,4,27)
today = str(datetime.datetime.today().date())
while date_dummy < datetime.datetime(int(today[:4]), int(today[5:7]), int(today[8:10])):
    date_dummy = date_dummy + datetime.timedelta(days=1)
    dates.append(date_dummy)
dates_df = pandas.DataFrame({'date': dates})

days = 'max'
x=0
# print(str(datetime.datetime.today())[:10])

#looping through all coins
for i in range (0,len(mapping['name'])):
    coin_tkr = mapping['ticker'][i]
    data = cg.get_coin_market_chart_by_id(mapping['name'][i], vs_currency='usd', days= days)
    
        # print(data)
    coin_dates = []
    coin_prices = []
    coin_vols = []
    coin_caps = []
    #price is only variable we are using
    #need to get a list of pandas timestamps to join list on
    for entry in data['prices']:
        dt = str(datetime.datetime.fromtimestamp(int(entry[0])/1000).date())
        new_date = datetime.datetime(int(dt[:4]), int(dt[5:7]), int(dt[8:10]))
        coin_dates.append(new_date)
        coin_prices.append(entry[1])
    for vol in data['total_volumes']:
        coin_vols.append(vol[1])
    for cap in data['market_caps']:
        coin_caps.append(cap[1])
    coin_data = pandas.DataFrame({'date': coin_dates, mapping['name'][i]+'_price': coin_prices, mapping['name'][i]+'_total_volume': coin_vols, mapping['name'][i]+'_market_cap': coin_caps})
    temp_df = dates_df.merge(coin_data, on= 'date', how= 'outer')
    dates_df.merge(temp_df, on= 'date', how= 'outer')
# print(dates_df)
# df = df.merge(temp_df)
# out_df = pandas.DataFrame({'dates': coin_dates, "prices_"+mapping['name'][i]:coin_prices})
dates_df.to_csv('coin_data.csv', index=False)


#  df.to_csv()   
# stamps = []
# for time in df['timestamps']:
#     new_time = str(datetime.datetime.fromtimestamp(int(time)/1000).date())
#     stamps.append(new_time)
# df['timestamps'] = stamps
# df['timestamps']
