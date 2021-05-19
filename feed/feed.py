# -*- coding: utf-8 -*-
"""
Created on Tue May 18 20:43:17 2021

@author: Acer
"""

import medium
import requests

#Importando e separando todos os símbolos
r = requests.get('https://api.binance.com/api/v3/exchangeInfo')
j = r.json()
j_symbols = j['symbols']
symbols = []
i = 0
for s in j_symbols:
    symbols.append(j['symbols'][i]['symbol'])
    i += 1


#escolhendo entre atualizar todos símbolos ou apenas específicos

#binance_symbols = ['BTCUSDT', 'ETHBTC', 'XRPBTC', 'XRPUSDT', 'XRPETH', 'ETHXRP', 'ETHUSDT']
binance_symbols = symbols

for  symbol in binance_symbols:
    medium.get_all_binance(symbol, "1d", save = "True")


