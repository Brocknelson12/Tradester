from pycoingecko import CoinGeckoAPI
import MongoDBUtils
cg = CoinGeckoAPI()
# test = cg.get_coin_market_chart_by_id("bitcoin", vs_currency="usd", days= "max")

mongo = MongoDBUtils.MongoUtils()
mongo.connect()
# mongo.connectToCollectino("dev","btc_hist")
mongo.collection.insert_one(test)

TICKERS = ['LINK', 'BTC', 'XLM', 'ZRX', 'ZEC', 'XTZ', 'XRP', 'REP', 'OXT', 'OMG' , 'MKR', 'LTC', 'KNC', 'ETH', 'ETC', 'EOS', 'DASH', 'DAI', 'COMP', 'BCH', 'BAT', 'ATOM']
TICKERS = [x.lower() for x in TICKERS]
symbols =  cg.get_coins_list()


for i in symbols:
    if i["symbol"] in TICKERS:
        data = cg.get_coin_market_chart_by_id(i["id"], vs_currency="usd", days= "max")
        mongo.connectToCollectino("dev",i["id"])
        timestamps = []
        for i in data["prices"]:
            timestamps.append(i[0]) 
        #data['timestamps'] = timestamps

        returnedData = {}

        for key in data:
            returnedData[key]  = []
            for entry in data[key]:
                returnedData[key].append(entry[1])
                
        returnedData['timestamps'] = timestamps

        mongo.collection.insert_one(returnedData)