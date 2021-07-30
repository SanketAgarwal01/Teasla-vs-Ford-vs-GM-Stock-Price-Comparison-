#!/usr/bin/env python
# coding: utf-8

# In[67]:


import pandas_datareader.data as web
import datetime
import matplotlib.pyplot as plt
import numpy as np


# In[68]:


start = datetime.datetime(2012,1,1)
end = datetime.datetime(2018,1,1)


# In[69]:


tesla = web.DataReader("TSLA",'yahoo',start,end)
ford = web.DataReader("F",'yahoo',start,end)
gm = web.DataReader("GM",'yahoo',start,end)


# In[70]:


tesla.to_csv('Tesla_Stock.csv')
ford.to_csv('Ford_Stock.csv')
gm.to_csv('GM_Stock.csv')


# In[71]:


tesla.head()


# In[72]:


ford.head()


# In[73]:


gm.head()


# In[74]:


tesla['Open'].plot(label = 'TESLA Open price', figsize=(16,7.5))
tesla['Close'].plot(label = 'TESLA Close price')
tesla['High'].plot()
tesla['Low'].plot()
plt.legend()
plt.title('Tesla Stock Price')
plt.ylabel('Stock Price')
plt.show()


# In[75]:


tesla['Open'].plot(label = 'Tesla', figsize=(16,7.5))
ford['Open'].plot(label = 'Ford')
gm['Open'].plot(label = 'GM')
plt.ylabel('Stock Price')
plt.title('Stock Prices of Tesla, Ford and GM')
plt.legend()


# In[76]:


tesla['Volume'].plot(label='Tesla', figsize=(15,7))
ford['Volume'].plot(label='Ford')
gm['Volume'].plot(label='GM')
plt.ylabel('Volume Traded')
plt.legend()


# In[77]:


ford.iloc[[ford['Volume'].argmax()]]


# In[78]:


ford.iloc[490:580]['Open'].plot(figsize=(17,7))


# In[79]:


tesla['Total Traded'] = tesla['Open'] * tesla['Volume']
ford['Total Traded'] = ford['Open'] * ford['Volume']
gm['Total Traded'] = gm['Open'] * gm['Volume']


# In[80]:


tesla.head()


# In[81]:


ford.head()


# In[82]:


gm.head()


# In[83]:


tesla['Total Traded'].plot(label='Tesla',figsize=(15,7))
ford['Total Traded'].plot(label='Ford')
gm['Total Traded'].plot(label='GM')
plt.legend()
plt.ylabel('Total Traded')


# In[84]:


tesla['Total Traded'].argmax()


# In[85]:


tesla.iloc[[tesla['Total Traded'].argmax()]]


# In[86]:


ford['Total Traded'].argmax()


# In[87]:


ford.iloc[[ford['Total Traded'].argmax()]]


# In[88]:


gm['Total Traded'].argmax()


# In[89]:


gm.iloc[[gm['Total Traded'].argmax()]]


# In[90]:


gm['Open'].iloc[440:500].plot(figsize=(15,7))


# In[91]:


gm['Open'].plot(label='No moving Avg',figsize=(15,7))
gm['MA50'] = gm['Open'].rolling(50).mean()
gm['MA50'].plot(label='MA50')
gm['MA150'] = gm['Open'].rolling(150).mean()
gm['MA150'].plot(label='MA150')
gm['MA250'] = gm['Open'].rolling(250).mean()
gm['MA250'].plot(label='MA250')
plt.legend()


# In[92]:


from pandas.plotting import scatter_matrix
import pandas as pd


# In[93]:


car_comp = pd.concat([tesla['Open'],ford['Open'],gm['Open']], axis =1)
car_comp.columns = ['Tesla Open', 'Ford Open', 'GM Open']


# In[94]:


scatter_matrix(car_comp, figsize=(10,8),hist_kwds={'bins':50})


# In[95]:


import mplfinance as mpf
import pandas as pd


# In[96]:


file = 'Ford_Stock.csv'
data = pd.read_csv(file)


# In[97]:


data


# In[98]:


data.info()


# In[99]:


data.columns


# In[100]:


data.Date = pd.to_datetime(data.Date)
data.info()


# In[101]:


data = data.set_index('Date')


# In[102]:


mpf.plot(data)


# In[103]:


mpf.plot(data['2017-07'], type= 'candle', volume = True)


# In[104]:


tesla ['return'] = (tesla['Close'] / tesla['Close'].shift(1))-1


# In[105]:


tesla.head()


# In[106]:


ford.head()


# In[107]:


gm.head()


# In[108]:


ford['return'] = (ford['Close'] / ford['Close'].shift(1))-1


# In[109]:


gm ['return'] = (gm['Close'] / gm['Close'].shift(1))-1


# In[110]:


gm.head()


# In[111]:


ford['return'].hist(bins=50,figsize=(8,7))


# In[112]:


tesla['return'].hist(bins=50,figsize=(8,7))


# In[113]:


gm['return'].hist(bins=50,figsize=(8,7))


# In[114]:


tesla['return'].hist(bins=100, label='TESLA',alpha=0.5, figsize=(11,7))
ford['return'].hist(bins=100, label='FORD',alpha=0.5)
gm['return'].hist(bins=100, label='GM',alpha=0.5)
plt.legend()


# In[115]:


tesla['return'].plot(kind='kde', label='TESLA',figsize=(13,6))
ford['return'].plot(kind='kde', label='FORD')
gm['return'].plot(kind='kde', label='GM')
plt.legend()


# In[116]:


box_df= pd.concat([tesla['return'],ford['return'],gm['return']], axis=1)
box_df.columns=['Tesla return','Ford return', 'GM return']
box_df.plot(kind ='box',figsize=(12,7))


# In[117]:


scatter_matrix(box_df,figsize=(9,9),hist_kwds={'bins':50},alpha=0.25)


# In[118]:


tesla['Cummulative return'] = (1 + tesla['return']).cumprod()
ford['Cummulative return'] = (1 + ford['return']).cumprod()
gm['Cummulative return'] = (1 + gm['return']).cumprod()
ford.head()
gm.head()


# In[119]:


tesla.head()


# In[120]:


tesla['Cummulative return'].plot(label='Tesla',figsize=(10,8))
ford['Cummulative return'].plot(label='Ford',figsize=(10,8))
gm['Cummulative return'].plot(label='GM',figsize=(10,8))
plt.title('Cummulative Return vs Time')
plt.legend()


# In[ ]:




