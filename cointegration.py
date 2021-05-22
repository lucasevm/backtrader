# -*- coding: utf-8 -*-
"""
Created on Mon May 17 10:04:13 2021

@author: Acer
"""

import quandl
import pandas as pd
from datetime import date, timedelta
import pathlib
import numpy as np

from matplotlib import pyplot as plt
import requests
import statsmodels.tsa.stattools as ts
from statsmodels.tsa.vector_ar.vecm import coint_johansen


dates = pd.date_range(date.today() - timedelta(days=400),date.today())
prices = pd.DataFrame(index=dates)
print(prices)
for file in pathlib.Path('feed').iterdir():
    if file.is_file():
        if file.suffix == '.csv':
            current_file = pd.read_csv(file)
            current_file['timestamp'] = current_file['timestamp'].astype('datetime64')
            df = current_file[['timestamp', 'close']]
            df = df.drop_duplicates(subset='timestamp')
            df = df.set_index('timestamp')
            prices = prices.join(df)
            print(prices)
            if prices['close'].isnull().values.any():
                prices.pop('close')
            else:
                prices.rename(columns={'close': file.name[0:file.name.find('-')]}, inplace=True)





# Salvo CSV dos preços
#prices.to_csv(r'prices.csv', index=True)
 
norm_prices = prices.divide(prices.iloc[0])

plt.figure(figsize = (15, 10))
plt.plot(prices)
plt.xlabel('days')
plt.title('Performance of cryptocurrencies')
#plt.legend(assets)
plt.show()

log_prices = np.log(prices)

for a1 in log_prices.columns:
    for a2 in log_prices.columns:
        if a1 != a2:
            test_result = ts.coint(log_prices[a1], log_prices[a2])
            if test_result[1] <= 0.01:
                print(a1 + ' and ' + a2 + ': p-value = ' + str(test_result[1]))
                

ts.coint_johansen()