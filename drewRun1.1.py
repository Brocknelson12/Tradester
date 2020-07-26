import datetime, pandas
from pycoingecko import CoinGeckoAPI
cg = CoinGeckoAPI()

TICKERS = ['LINK', 'BTC', 'XLM', 'ZRX', 'ZEC', 'XTZ', 'XRP', 'REP', 'OXT', 'OMG' , 'MKR', 'LTC', 'KNC', 'ETH', 'ETC', 'EOS', 'DASH', 'DAI', 'COMP', 'BCH', 'BAT', 'ATOM']
TICKERS_low = [x.lower() for x in TICKERS]
NAMES =  cg.get_coins_list()
mapping = {
            'ticker': ['zrx', 'rep', 'bat', 'bat', 'btc', 'bch', 'link', 'comp', 'comp', 'atom', 'dai', 'dash', 'eos', 'eth', 'etc', 'knc', 'ltc', 'mkr', 'omg', 'oxt', 'xrp', 'xlm', 'xtz', 'xtz', 'zec'], 
            'name': ['0x', 'augur', 'basic-attention-token', 'batcoin', 'bitcoin', 'bitcoin-cash', 'chainlink', 'compound-coin', 'compound-governance-token', 'cosmos', 'dai', 'dash', 'eos', 'ethereum', 'ethereum-classic', 'kyber-network', 'litecoin', 'maker', 'omisego', 'orchid-protocol', 'ripple', 'stellar', 'tezos', 'tezos-iou', 'zcash']
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
for coin_name in mapping['name']:
    coin = pandas.DataFrame()
    coin_tkr = mapping['ticker'][x]
    data = cg.get_coin_market_chart_by_id(coin_name, vs_currency='usd', days= days)
    prices = []
    for price in list(data['prices']):
        price = price[1]
        prices.append(price)
    # market_caps = list(data['market_caps'])
    # total_volumes = list(data['total_volumes'])
    coin_times = []
    for time in list(data['prices']):
        time = time[0]
        new_time = str(datetime.datetime.fromtimestamp(int(time)/1000).date())
        # print(new_time)
        coin_times.append(new_time)

    coin['timestamps'] = coin_times
    coin[coin_name] = prices
    # print(coin_data['timestamps'])
    # print(coin['timestamps'])
    # print(coin)
    # coin_data.join(coin,on='timestamps',how= 'outer')
    merged_df = pandas.concat([coin_data,coin], sort=False)
    # final_df = pandas.concat([all_coins,merged_df], join='outer', sort=False)

    # all_coins[coin_tkr] = final_df
    # print(merged_coin)
    # break
    # merge df
    # out_put df
    # merge to all_coin_data df
    # coin_data[coin_tkr] = prices
    # coin_data[coin_tkr] = [timestamps,prices,market_caps,total_volumes]
    x+=1
merged_df.to_csv('coin_data.csv', index=False)
# coin_data.to_csv('coin_data.csv', index=False)
# coin_data = pandas.DataFrame(coin_data)
# coin_data.to_csv('coin_data.csv')

# x = 0
# z = 1

# while z <= int(len(prices)-1):
#     for price in prices:
#         try:
#             x_price = prices[x][1]
#             z_price = prices[z][1]
#             pct_change = (z_price-x_price)/x_price
#             # if x_price < z_price:   # diff in  change, positive
#             # if pct_change > .05:
#             #     print('Match! @ '+str(pct_change))
#             #     print(str(timestamps[x])+' ____ '+str(prices[x][1]))
#             #     print(str(timestamps[z])+' ____ '+str(prices[z][1]))
            
#         except IndexError:
#             pass
#         x+=1
#         z+=1
# print('Len Prices: '+str(len(list(data['prices']))))
# print('Len Time: '+str(len(timestamps)))
# print(timestamps[0])
# print(prices[0])
# print(prices[1])
# print(name['id'])

# # _id = list(values[0]['_id'])
# prices = list(values[0]['prices'])
# market_caps = list(values[0]['market_caps'])
# total_volumes = list(values[0]['total_volumes'])

# timestamps = []
# for time in list(values[0]['timestamps']):
#     new_time = datetime.datetime.fromtimestamp(int(time)/1000)
#     timestamps.append(new_time)

# print(len(timestamps))
# print(timestamps[0])