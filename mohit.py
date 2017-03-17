import quandl
import requests
import matplotlib.pyplot as plt
import pandas
from pandas import DataFrame
import datetime
import numpy as np
import matplotlib.patches as mpatches
#http://techpaisa.com/stock/tcs/

quandl.ApiConfig.api_key = 'Hqu7HLNnBU4bxBU4jLaZ'

def drawChartSMA(close,date,sma):
    y =close
    x =date
    plt.plot(x,y,'g',label='Daily Closing Price')
    plt.plot(x,sma,'r',label='SMA')
    plt.xlabel('Date')
    plt.ylabel('Closing Prices/SMA')
    plt.title('SMA')
    plt.legend()
    if(sma[len(sma)-1]<close[len(close)-1]):
        print("SMA says Uptrend")
    elif(sma[len(sma)-1]>close[len(close)-1]):
        print("SMA says Downtrend")
    else:
        print("Trend Reversal may occur")
    plt.show() 

def movingaverage(values,window):
    weights = np.repeat(1.0,window)/window
    smas = np.convolve(values,weights,'valid').tolist()  
    listt=list()
    for c in range(0,window-1):
          listt.append(0)
    smas = listt+smas
    for m in range(0,len(smas)):
        smas[m] = float("{0:.2f}".format(smas[m]))
     
    return smas








try:
    name = input("Enter Ticker:")
    url = "https://www.quandl.com/api/v3/datasets/NSE/"+name+"/metadata.json"
    try:
        meta_data = requests.get(url)
        
        parsed_meta_data = meta_data.json()
        print("Name: {}".format(parsed_meta_data['dataset']['name']))
        searched_data = quandl.get("NSE/"+name)
       
        close = searched_data.Close
        n=20
       
        sma=movingaverage(close.tolist(),n)
        date=pandas.to_datetime(searched_data.index)
        drawChartSMA(close.tolist(),date.tolist(),sma)
        
    except Exception:
        print("May be No. Of Attempts for today by the key is finished")
except Exception:
    print("Check your Internet Connection")
