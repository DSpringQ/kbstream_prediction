
import matplotlib.pyplot as plt
from matplotlib.finance import quotes_historical_yahoo_ochl
from matplotlib.dates import YearLocator, MonthLocator, DateFormatter
import datetime
date1 = datetime.date(1999, 1, 1)
date2 = datetime.date(2000, 4, 12)
print("1")
years = YearLocator()   # every year
months = MonthLocator()  # every month
yearsFmt = DateFormatter('%Y')

quotes = quotes_historical_yahoo_ochl('INTC', date1, date2)
if len(quotes) == 0:
    raise SystemExit
print("2")
dates = [q[0] for q in quotes]
opens = [q[1] for q in quotes]

print(dates)
print(dates[0])
print(dates[1])
print(type(dates[0]))

fig, ax = plt.subplots()
ax.plot_date(dates, opens, '-')
print("3")
# format the ticks
ax.xaxis.set_major_locator(years)
ax.xaxis.set_major_formatter(yearsFmt)
ax.xaxis.set_minor_locator(months)
ax.autoscale_view()


# format the coords message box
def price(x):
    return '$%1.2f' % x
ax.fmt_xdata = DateFormatter('%Y-%m-%d')
ax.fmt_ydata = price
ax.grid(True)

fig.autofmt_xdate()
plt.show()