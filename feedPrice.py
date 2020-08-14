import pymongo, pandas, talib, numpy, MongoDBUtils
from talib.abstract import *
# import plotly.express as px
import plotly.graph_objects as go

mongo = MongoDBUtils.MongoUtils()
mongo.connect()
mongo.connectToCollectino('dev', 'btc_2019_1hr')
values = mongo.getAll()

dates = list(values[0]['date'])
prices = list(values[0]['prices'])
market_caps = list(values[0]['market_cap'])
total_volumes = list(values[0]['total_volume'])

fast_ema = EMA(numpy.array(prices),timeperiod=12)
# print(fast_ema)
slow_ema = EMA(numpy.array(prices),timeperiod=26)
# print(slow_ema)
# macd = MACD()
data = {'dates': dates, 'prices': prices, 'fast_ema': fast_ema, 'slow_ema': slow_ema}
# print(len(data['fast_ema']))
fig = go.Figure()
fig.add_trace(go.Scatter(x=data['dates'], y=data['prices'], mode='lines', name='price'))
fig.add_trace(go.Scatter(x=data['dates'], y=data['fast_ema'], mode='lines', name='fast_ema'))
fig.add_trace(go.Scatter(x=data['dates'], y=data['slow_ema'], mode='lines', name='slow_ema'))

# green crosses over top of red = short
# red crosses over top of green = long
# df = px.data.gapminder().query("continent=='Oceania'")
fig.show()