import quandl
import requests
import matplotlib.pyplot as plt
import pandas
# from pandas import DataFrame
# import datetime
import numpy as np
# import matplotlib.patches as mpatches

quandl.ApiConfig.api_key = 'Hqu7HLNnBU4bxBU4jLaZ'


def drawChartSMA(close, date, sma):
    y = close
    x = date
    plt.plot(x, y, 'g', label='Daily Closing Price')
    plt.plot(x, sma, 'r', label='SMA')
    plt.xlabel('Date')
    plt.ylabel('Closing Prices/SMA')
    plt.title('SMA')
    plt.legend()
    val_len = len(close)
    k = val_len - 20
    min = close[k]
    max = close[k]
    for t in range(k, val_len):
        if(close[t] < min):
            min = close[t]
        if(close[t] > max):
            max = close[t]

    if(sma[len(sma) - 1] < close[len(close) - 1]):
        print("SMA says Uptrend")
        print("Support is Rs.", min)
        print("Resistance is Rs.", max)
    elif(sma[len(sma) - 1] > close[len(close) - 1]):
        print("SMA says Downtrend")
        print("Support is Rs.", min)
        print("Resistance is Rs.", max)
    else:
        print("Trend Reversal may occur")
        print("Support is Rs.", min)
        print("Resistance is Rs.", max)
    plt.show()


def movingaverage(values, window):
    weights = np.repeat(1.0, window) / window
    smas = np.convolve(values, weights, 'valid').tolist()
    listt = list()
    for c in range(0, window - 1):
        listt.append(0)
    smas = listt + smas
    for m in range(0, len(smas)):
        smas[m] = float("{0:.2f}".format(smas[m]))

    return smas


def ExpMovingAverage(values, window):
    weights = np.exp(np.linspace(-1., 0., window))
    weights /= weights.sum()
    a = np.convolve(values, weights, mode='full')[:len(values)]
    a[:window] = a[window]
    return a


def computeMACD(x, slow=26, fast=12):
    emaslow = ExpMovingAverage(x, slow)
    emafast = ExpMovingAverage(x, fast)
    return emaslow, emafast, emafast - emaslow


def rsiFunc(close, n, date):
    deltas = np.diff(close)
    seed = deltas[:n + 1]
    up = seed[seed >= 0].sum() / n
    down = -seed[seed < 0].sum() / n
    rs = up / down
    rsi = np.zeros_like(close)
    rsi[:n] = 100. - 100. / (1 + rs)
    for i in range(n, len(close)):
        delta = deltas[i - 1]
        if delta > 0:
            upval = delta
            downval = 0.
        else:
            upval = 0.
            downval = -delta
        up = (up * (n - 1) + upval) / n
        rs = up / down
        rsi[i] = 100. - 100. / (1. + rs)
        rsi[i] = float("{0:.2f}".format(rsi[i]))
    plt.plot(date, close.tolist())
    plt.plot(date, rsi.tolist())
    plt.show()
    return rsi


def plotMACD(close, ema9, emaslow, emafast, macd, date):
    plt.plot(date, emaslow.tolist(), label="slow")
    plt.plot(date, emafast.tolist(), label="fast")
    plt.plot(date, macd.tolist(), label="macd")
    plt.plot(date, ema9.tolist(), label="ema9")
    plt.plot(date, close, label="closing prices")
    plt.legend()
    plt.show()


try:
    name = input("Enter Ticker:")
    url = "https://www.quandl.com/api/v3/datasets/NSE/" + name + "/metadata.json"
    try:
        meta_data = requests.get(url)
        parsed_meta_data = meta_data.json()
        print("Name: {}".format(parsed_meta_data['dataset']['name']))
        searched_data = quandl.get("NSE/" + name)
        close = searched_data.Close
        n = 20
        sma = movingaverage(close.tolist(), n)
        date = pandas.to_datetime(searched_data.index)
        drawChartSMA(close.tolist(), date.tolist(), sma)
        nema = 9
        emaslow, emafast, macd = computeMACD(close)
        ema9 = ExpMovingAverage(macd, nema)
        print("MACD:", float("{0:.2f}".
                             format(macd[len(macd) - 1])), "and Signal Line:",
              float("{0:.2f}".format(ema9[len(ema9) - 1])))
        plotMACD(close, ema9, emaslow, emafast, macd, date.tolist())
        rsi = rsiFunc(close, 14, date.tolist())
        print("RSI is:", rsi[len(rsi) - 1])
    except Exception:
        print("May be No. Of Attempts for today by the key is finished")
except Exception:
    print("Check your Internet Connection")
