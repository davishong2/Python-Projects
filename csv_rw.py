import csv
from datetime import datetime

data = []
path = "d:\python_files\my_projects\csv_practice\googlestockprice.csv"
with open (path, 'r', newline = '') as file:
    reader = csv.reader(file)
    header = next(reader)

    for row in reader:
        # row = [Date, Open, High, Low, Close, Volume, Adj Close]
        date = datetime.strptime(row[0], '%m/%d/%Y')
        open_px = float(row[1])
        high = float(row[2])
        low = float(row[3])
        close = float(row[4])
        vol = int(row[5])
        adj_close = float(row[6])

        data.append([date, open_px, high, low, close, vol, adj_close])
    
returns_path = 'd:\python_files\my_projects\csv_practice\googles_returns.csv'
with open (returns_path, 'w', newline = '') as file:
    writer = csv.writer(file)
    writer.writerow(['Date', 'Return'])

    for i in range(len(data) -1):
        todays_row = data[i]
        todays_date = todays_row[0] # today's date is the first element in todays_row
        todays_price = todays_row[-1] # last element of todays_row
        yesterdays_row = data[i + 1]
        yesterdays_price = yesterdays_row[-1]
        daily_return = (todays_price - yesterdays_price) / yesterdays_price
        formatted_date = todays_date.strftime('%m/%d/%Y')
        writer.writerow([formatted_date, daily_return])


