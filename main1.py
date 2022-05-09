import yfinance as yf

goog = yf.Ticker('goog')
result = goog.get_info()["totalRevenue"]
sep = "{:,}".format(result)

print(sep)
