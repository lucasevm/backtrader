# -*- coding: utf-8 -*-
"""
Created on Tue May 18 11:35:05 2021

@author: Acer
"""

from __future__ import (absolute_import, division, print_function,
                         unicode_literals)

import datetime #para objetos de datetime
import os.path #gerenciar os caminhos de arquivo
import sys #para encontrar os scripts

import backtrader as bt #plataforma de backtrade

if __name__ == '__main__':
    cerebro = bt.Cerebro() #cria a entidade cérebro
    
    data = bt.feeds.
    
    
    
    
    cerebro.broker.setcash(300.0)
    
    print('Starting Portfolio Value: %.2f' % cerebro.broker.getvalue())

    cerebro.run()

    print('Final Portfolio Value: %.2f' % cerebro.broker.getvalue())