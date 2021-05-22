# backtrader
aprendendo o uso do backtrader

Main - módulo main para gerenciar quando roda cada coisa

i - módulo para pegar dados binance (1D, 1H, 15M, o que for necessário)

ii - módulo de pair trading (descobrir os melhores pares cointegrados)

iii - módulo trade comum (RSI stochastic, cruzamento de médias, etc)

iv - módulo de sentiment trade

v - Put-call parity (arbitrage): https://www.investopedia.com/terms/p/putcallparity.asp#:~:text=Put%2Dcall%20parity%20is%20a,strike%20price%2C%20and%20expiration%20date.
Nota: Levar em conta o ativo descontado risk-free rate (pode ser stake, selic, etc) https://www.calkoo.com/en/put-call-parity-calculator
-> Current Price of Underlying Asset = Call Option Price - Put Option Price + PV(x)
-> Call Option Price + PV(x) = Put Option Price + Current Price of Underlying Asset
