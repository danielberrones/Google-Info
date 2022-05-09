import yfinance as yf

goog = yf.Ticker('goog')

for k,v in goog.get_info().items():
    print(k,v)
