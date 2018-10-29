import pandas as pd, numpy as np
import matplotlib.pyplot as plt
import os

##Getting data in.
def stock_func(stock_name,base_dir="E:"):
    global df
    global df2
    global stock
    
    stock = str(stock_name)
    filepath= os.path.join(base_dir,"\BI_MATERIAL\R_Workspace\datafiles","{}.csv".format(str(stock_name)+ "_NSE"))
    df = pd.read_csv(filepath,index_col='Date',parse_dates=True,usecols=['Date','Close','Adj Close','Volume'])
    df2 = df["2015-08-01":"2017-08-01"]
    return filepath



##Compute Bollinger Bands
def compute_rolling_stats(df,col,window=20):
    """ Compute rolling mean """
    rm = pd.rolling_mean(df[col], window=window)

    """ Compute rolling standard deviation """
    rstd = pd.rolling_std(df[col], window=window)

    """ Compute upper and lower bands """
    upper_band = rm + 2*rstd
    lower_band = rm - 2*rstd

    """ Plot raw SPY values, rolling mean and Bollinger Bands """
    ax = df[col].plot(title="Bollinger Bands", label=stock)
    rm.plot(label='Rolling mean', ax=ax)
    upper_band.plot(label= 'Upper band', ax=ax)
    lower_band.plot(label= 'Lower band', ax=ax)

    """ Add axis labels, legend  and plot """
    ax.set_ylabel("Price")
    ax.legend(loc='upper left')
    plt.show()
    
    return "Process Successful"


#Compute Daily Return

##def compute_daily_returns(df,col):
##    """ Compute daily return """
##    daily_return = df
##    daily_return[col][1:] = (df[col][1:]/ df[col][:-1].values)-1
##    daily_return.ix[0,:] = 0  # Initializing value to 0
##    mean = daily_return[col].mean()
##    std  = daily_return[col].std()
##
##    """ Plot daily return """
##    ax = daily_return[col].plot(color='b')
##    ax.set_xlabel("Date")
##    ax.set_ylabel("Price")
##    plt.axhline(mean,color='r',linestyle='dashed',linewidth=2)
##    plt.axhline(std,color='g',linestyle='dashed',linewidth=2)
##    plt.axhline(-std,color='g',linestyle='dashed',linewidth=2)
##    plt.show()
##
##    """  Plot daily return histogram """
##    daily_return[col].hist(bins=20)
##    plt.axvline(mean,color='w',linestyle='dashed',linewidth=2)
##    plt.axvline(std,color='r',linestyle='dashed',linewidth=1)
##    plt.axvline(-std,color='r',linestyle='dashed',linewidth=1)
##    plt.show()

    

stock_func('HDFCLIFE')
print compute_rolling_stats(df,'Adj Close')
#print compute_daily_returns(df,'Adj Close')
