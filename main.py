# -*- coding: utf-8 -*-
"""
Created on Fri May 14 19:20:13 2021

@author: Acer
"""

import pandas as pd

url = "https://api1.binance.com/api/v3/ticker/24hr"


new_data = pd.read_json(url, orient="records")