# -*- coding: utf-8 -*-
"""
Created on Tue May 18 12:24:42 2021

@author: Acer
"""

#Binance Spot Test Network

api_key_test = 'PTw2KyiNCU8OJvPxkaP7q62FXa7SjqhsjLW1CezpIMyLQsfex6GgsTwlkgGpFSeT'
api_secret_test = 'KlDX8xFTVrs3FSr4japb9N9HXmKX9j9QNw7f3iNPYK8bQswHfF376ugKudhKBt8f'

#imports

import os
from binance.client import Client
import csv


#para setar variável no environment do windows pelo cmd:

#set binance_api=your_api_key_here
#set binance_secret=your_api_secret_here

# init
api_key = os.environ.get('binance_api')
api_secret = os.environ.get('binance_secret')
print(api_key)
print(api_secret)
print(os.environ.get('test2'))

'binance_api' in os.environ

#Conexões

#client = Client(api_key, api_secret)
client = Client(api_key_test, api_secret_test)

client.API_URL = 'https://testnet.binance.vision/api'


#Saldos de Conta

print(client.get_account()) #saldos de conta
print(client.get_asset_balance(asset='BTC')) #saldo de ativo em específico
print(client.futures_account_balance()) #saldo de futuros
print(client.get_margin_account()) #saldo de margem


#Cotações

price = client.get_symbol_ticker(symbol="BTCUSDT")
print(price)


timestamp = client._get_earliest_valid_timestamp('BTCUSDT', '1d')
print(timestamp)

#historical klines data
bars = client.get_historical_klines('BTCUSDT','1d', timestamp, limit = 1000)
print(bars)

open('btc_bars.csv', 'w', newline='')

# option 2 - save as CSV file using the csv writer library
with open('btc_bars.csv', 'w', newline='') as f:
    wr = csv.writer(f)
    for line in bars:
        wr.writerow(line)