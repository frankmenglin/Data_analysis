import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pandas_datareader
import datetime
import pandas_datareader.data as web

start = datetime.datetime(2012,1,1)#Start Time
end = datetime.datetime(2020,7,24)#End Time

tesla = web.DataReader('TSLA','yahoo', start, end)
apple = web.DataReader('AAPL','yahoo', start, end)
amazon = web.DataReader('AMZN','yahoo', start, end)#Stock Prices from yahoo
#print(amazon.head())#View Data

#tesla['Close'].plot(label="TSLA", figsize=(16,8), title='Open Price')
#apple['Close'].plot(label="AAPL")
#amazon['Close'].plot(label="AMZN")
#plt.show();#Mutiple Stock Prices in 1 graph

tesla['returns']=tesla['Close'].pct_change(1)
apple['returns']=apple['Close'].pct_change(1)
amazon['returns']=amazon['Close'].pct_change(1)
#print(amazon.head())
amazon['returns'].hist(bins=100)
plt.show()
