import csv
from datetime import datetime

path = "google_stock_data.csv.csv"

file = open(path, newline='')
reader = csv.reader(file)

header = next(reader)

data = []
for row in reader:
    date = datetime.strptime(row[0], '%m/%d/%Y')
    open_price = float(row[1])
    high = float(row[2])
    low = float(row[3])
    close = float(row[4])
    volume = int(row[5])
    adj_close = float(row[6])


    data.append([date, open_price, high, low, close, volume, adj_close])

# compute and store the returns
path = 'google_returns.csv'
file = open(path, 'w')
writer = csv.writer(file)
writer.writerow(["Date", "Returns"])

for i in range(len(data) - 1):
    todays_row = data[i]
    todays_date = todays_row[0]
    todays_price = todays_row[-1]
    yesterdays_row = data[i+1]
    yesterdays_price = yesterdays_row[-1]

    daily_return = (todays_price - yesterdays_price) / yesterdays_price
    writer.writerow([datetime.strftime(todays_date, '%d/%m/%Y'), daily_return])
