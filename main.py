# write af unction to calculate the value of 3X +1

def f(x):
    return 3 * x + 1


print(f(2))

# now we use Lambda

lambda x: 3 * x + 1

g = lambda x: 3 * x + 1
print(g(2))


def f(x):
    return 3 * x + 1


print(f(2))

k = lambda x: 3 * x + 1
print(k(2))

full_name = lambda fn, ln: fn.strip().title() + " " + ln.strip().title()
print(full_name("Kahled", "AlGHaiSh"))


# Step 1: Import The Required Libraries
# I’m using Jupyter Notebook. I want to plot my charts inline, so I call %matplotlib inline first.
#
# We’ll start by importing the libraries we need
import matplotlib as matplotlib


import math
import yfinance as yf
import numpy as np
import matplotlib.pyplot as plt

# Step 2: Setup The Variables
# Next, we’ll setup some variables we’ll use later. These are all Python lists.
# windows defines the number of days I want to use to compute volatility.
# quantiles defines the percentage of the top and bottom 25% of values.
# The last few lists are where we accumulate data to plot.

windows = [30, 60, 90, 120]
quantiles = [0.25, 0.75]

min_ = []
max_ = []
median = []
top_q = []
bottom_q = []
realized = []

# lets get some data

data = yf.download("JPM", start="2020-01-01", end="2020-12-31")

# As usual, we’ll use yfinance to get stock data –
# in this case, JPM. You can use any stock and any price range you want.

# Step 3: Realized Volatility

#Realized volatility is a measurement of how much the price or returns of stock vary.
# It’s used to optimize portfolios,detect regime changes, and price derivatives.
# The most common way to measure realized volatility is the standard deviation.

def realized_vol(price_data, window=30):

    log_return = (price_data["Close"] / price_data["Close"].shift(1)).apply(np.log)

    return log_return.rolling(window=window, center=False).std() * math.sqrt(252)

# The next step is to loop through each of the windows and compute realized volatility
# over each time frame.estimator is a pandas DataFrame. That’s why it’s so easy so
# compute the min, max, median, and quantiles. Magic.

for window in windows:
    # get a dataframe with realized volatility
    estimator = realized_vol(window=window, price_data=data)

    # append the summary stats to a list
    min_.append(estimator.min())
    max_.append(estimator.max())
    median.append(estimator.median())
    top_q.append(estimator.quantile(quantiles[1]))
    bottom_q.append(estimator.quantile(quantiles[0]))
    realized.append(estimator[-1])

# Step 4: Plot The Results
# The last step is to create a chart that plots the volatility cone.

# create the plots on the chart
plt.plot(windows, min_, "-o", linewidth=1, label="Min")
plt.plot(windows, max_, "-o", linewidth=1, label="Max")
plt.plot(windows, median, "-o", linewidth=1, label="Median")
plt.plot(windows, top_q, "-o", linewidth=1, label=f"{quantiles[1] * 100:.0f} Prctl")
plt.plot(windows, bottom_q, "-o", linewidth=1, label=f"{quantiles[0] * 100:.0f} Prctl")
plt.plot(windows, realized, "ro-.", linewidth=1, label="Realized")

# set the x-axis labels
plt.xticks(windows)

# format the legend
plt.legend(loc="upper center", bbox_to_anchor=(0.5, -0.1), ncol=3)
# The first 6 lines create the lines on the chart. The other two align the x-axis labels and format the legend.
