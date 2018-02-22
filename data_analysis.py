import pandas_datareader as web
import datetime
import matplotlib.pyplot as plt
from matplotlib import style
style.use('fivethirtyeight')

start = datetime.datetime(2010, 1, 1)
end = datetime.datetime(2015, 8, 22)

df = web.DataReader("XOM", "google", start, end)

df['Volume'].plot()
df['High'].plot()
plt.legend()
plt.show()
