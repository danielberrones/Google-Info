import yfinance as yf

goog = yf.Ticker('goog')
totalRevenue = goog.get_info()["totalRevenue"]

sep = "{:,}".format(totalRevenue)
print("totalRevenue\n", sep)

