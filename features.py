import numpy as np
import pandas as pd
import os
import random
import copy
import matplotlib.pyplot as plt

#RSI FUNCTION
def rsi(values):
	up = values[values>0].mean()
	down = -1*values[values<0].mean()
	return 100*up/(up+down)


#BOLLINGER BAND FUNCTION
def bbands(price, length=30, numsd=2):
    """ returns average, upper band, and lower band"""
    #ave = pd.stats.moments.rolling_mean(price,length)
    ave = price.rolling(window = length, center = False).mean()
    #sd = pd.stats.moments.rolling_std(price,length)
    sd = price.rolling(window = length, center = False).std()
    upband = ave + (sd*numsd)
    dnband = ave - (sd*numsd)
    return np.round(ave,3), np.round(upband,3), np.round(dnband,3)	


#AROON OSCILLATION FUNCTION
def aroon(df, tf=25):
    aroonup = []
    aroondown = []
    x = tf
    while x< len(df['Date']):
        aroon_up = ((df['High'][x-tf:x].tolist().index(max(df['High'][x-tf:x])))/float(tf))*100
        aroon_down = ((df['Low'][x-tf:x].tolist().index(min(df['Low'][x-tf:x])))/float(tf))*100
        aroonup.append(aroon_up)
        aroondown.append(aroon_down)
        x+=1
    return aroonup, aroondown    


dft = pd.read_csv('stock tickers.csv')
tickers = dft['ticker'].to_list()




#Calculate RSI
# for symbol in tickers:
# 	try:
# 		df1 = pd.read_csv(symbol+'.csv')
# 		df1['Momentum_1D'] = (df1['Close']-df1['Close'].shift(1)).fillna(0)
# 		df1['RSI_14D'] = df1['Momentum_1D'].rolling(center=False,window=14).apply(rsi).fillna(0)
# 		df1.to_csv(symbol+'.csv',index=False)
# 		print(df1.tail(5))
# 	except Exception:
# 		None	

#print(5)

#Calculate Bollinger Bands
# for symbol in tickers:
# 	try:
# 		df1 = pd.read_csv(symbol+'.csv')
# 		df1['BB_MIDDLE_BAND'], df1['BB_UPPER_BAND'],df1['BB_LOWER_BAND'] = bbands(df1['Close'],length=20,numsd=1)
# 		df1['BB_MIDDLE_BAND'] = df1['BB_MIDDLE_BAND'].fillna(0)
# 		df1['BB_UPPER_BAND'] = df1['BB_UPPER_BAND'].fillna(0)
# 		df1['BB_LOWER_BAND'] = df1['BB_LOWER_BAND'].fillna(0)
# 		df1.to_csv(symbol+'.csv',index=False)
# 		print(df1.tail(5))

# 	except Exception:
# 		None	

#Calculate Aroon Oscillator
# for symbol in tickers:
# 	try:
# 		df1 = pd.read_csv(symbol+'.csv')
# 		listofzeros = [0]*25
# 		up, down =  aroon(df1)
# 		aroon_list = [x-y for x, y in zip(up,down)]
# 		if len(aroon_list)==0:
# 			aroon_list=[0]*df1.shape[0]
# 			df1['Aroon_oscillator'] = aroon_list
# 		else:
# 			df1['Aroon_oscillator'] = listofzeros+aroon_list	
# 		df1.to_csv(symbol+'.csv',index=False)
# 		print(df1.tail(5))

# 	except Exception:
# 		None	

#Calculate PVT
# for symbol in tickers:
# 	try:
# 		df1 = pd.read_csv(symbol+'.csv')
# 		df1['PVT'] = (df1['Momentum_1D']/df1['Close'].shift(1))*df1['Volume']
# 		df1['PVT'] = df1['PVT'] - df1['PVT'].shift(1)
# 		df1['PVT'] = df1['PVT'].fillna(0)
# 		df1.to_csv(symbol+'.csv',index=False)
# 		print(df1.tail(5))
		
# 	except Exception:
# 		None	



#DROP COLUMNS
# columns2drop  = ['Momentum_1D']
# for symbol in tickers:
#     try:
#         df1 = pd.read_csv(symbol+'.csv')
#         df1 = df1.drop(labels=columns2drop,axis=1)
#         print(df1.head(5))
#         df1.to_csv(symbol+'.csv',index=False)
#     except Exception:
#         None


#Calculate Momentum
# for symbol in tickers:
#   try:
#       df1 = pd.read_csv(symbol+'.csv')
#       df1['Momentum'] = df1['Close'] - df1['Close'].shift(4)
#       df1 = df1.fillna(0)
#       df1.to_csv(symbol+'.csv',index=False)
#       print(df1.tail(5))
        
#   except Exception:
#       None    


# df = pd.read_csv('GOOGL.csv')
# #df1=df1.iloc[1613:1700]
# df.loc[:,'Date'] = pd.to_datetime(df['Date'], format='%Y-%m-%dT%H:%M:%S.%f')
# df.set_index('Date')
# plt.style.use('seaborn-whitegrid')
# fig = plt.figure(figsize=(20,25))
# ax = plt.subplot(1,1,1)
# axvol = ax.twinx()
# #ax.fill_between(df1.index, df1['BB_UPPER_BAND'],df1['BB_MIDDLE_BAND'],df1['BB_LOWER_BAND'],color = 'grey', label = "Band Range")
# ax.plot(df1.index, df1['Close'], color='red',lw=2, label="Close")
# #ax.plot(df1.index, df1['BB_MIDDLE_BAND'], color='black',lw=2, label="Middle Band")
# ax.plot(df1.index, df1['BB_UPPER_BAND'], color='blue',lw=2, label="Upper Band")
# ax.plot(df1.index, df1['BB_LOWER_BAND'], color='green',lw=2, label="Lower Band")
# axvol.plot(df1.index, df1['Volume'], color='yellow',lw=2, label="Volume")
# #ax.plot(df1.index, df1['Momentum'], color='green',lw=2, label="Momentum")
# ax.set_title("Close Price for" + 'TESLA for the year 2018')
# ax.legend()
# ax.set_xlabel("Date")
# ax.set_ylabel("Close Prices")
# plt.xticks(rotation=30)

# ax = df1.plot(x='Date',y='Close',title='Corelation Between Close and Aroon_oscillator with respect to Time for TESLA Stocks',figsize=(40,8))
# df1.plot(x='Date',y='Aroon_oscillator',ax=ax)
#df1.plot(x='Date',y='BB_UPPER_BAND',ax=ax)

#df1.plot(x='Date',y='Volume',ax=ax)
    
#fig.tight_layout()
#plt.show()

# plt.style.use('seaborn-whitegrid')
# fig = plt.figure(figsize=(40,8))
# ax = plt.subplot()
# ax.fill(df.index, df['Aroon_oscillator'],'g', alpha = 0.5, label = "Aroon oscillator")
# ax.plot(df.index, df['Close'], 'r', label="Close")
# ax.set_title("Aroon Oscillator for GOOGLE" )
# ax.legend()
# ax.set_xlabel("Date")
# ax.set_ylabel("Close Prices")
# plt.xticks(rotation=30)
    
# fig.tight_layout()
# plt.show()

# for symbol in tickers:
#   try:
#       df1 = pd.read_csv(symbol+'.csv')
#       df1.loc[:,'Date'] = pd.to_datetime(df1['Date'], format='%Y-%m-%d %H:%M:%S.%f') 
#       df1.to_csv(symbol+'.csv',index=False)
#       print(df1.tail(5))
#   except Exception:
#       None    





#SUPER TREND

# for symbol in tickers:
#   try:
#       data = pd.read_csv(symbol+'.csv')
#       data['tr0'] = abs(data["High"] - data["Low"])
#       data['tr1'] = abs(data["High"] - data["Close"].shift(1))
#       data['tr2'] = abs(data["Low"]- data["Close"].shift(1))
#       data["TR"] = round(data[['tr0', 'tr1', 'tr2']].max(axis=1),2)
#       data["ATR"]=0.00
#       data['BUB']=0.00
#       data["BLB"]=0.00
#       data["FUB"]=0.00
#       data["FLB"]=0.00
#       data["ST"]=0.00
#       # Calculating ATR 
#       for i, row in data.iterrows():
#           if i == 0:
#               data.loc[i,'ATR'] = 0.00#data['ATR'].iat[0]
#           else:
#               data.loc[i,'ATR'] = ((data.loc[i-1,'ATR'] * 13)+data.loc[i,'TR'])/14

#       data['BUB'] = round(((data["High"] + data["Low"]) / 2) + (2 * data["ATR"]),2)
#       data['BLB'] = round(((data["High"] + data["Low"]) / 2) - (2 * data["ATR"]),2)


#       # FINAL UPPERBAND = IF( (Current BASICUPPERBAND < Previous FINAL UPPERBAND) or (Previous Close > Previous FINAL UPPERBAND))
#       #                     THEN (Current BASIC UPPERBAND) ELSE Previous FINALUPPERBAND)


#       for i, row in data.iterrows():
#           if i==0:
#               data.loc[i,"FUB"]=0.00
#           else:
#               if (data.loc[i,"BUB"]<data.loc[i-1,"FUB"])|(data.loc[i-1,"Close"]>data.loc[i-1,"FUB"]):
#                   data.loc[i,"FUB"]=data.loc[i,"BUB"]
#               else:
#                   data.loc[i,"FUB"]=data.loc[i-1,"FUB"]

#       # FINAL LOWERBAND = IF( (Current BASIC LOWERBAND > Previous FINAL LOWERBAND) or (Previous Close < Previous FINAL LOWERBAND)) 
#       #                     THEN (Current BASIC LOWERBAND) ELSE Previous FINAL LOWERBAND)

#       for i, row in data.iterrows():
#           if i==0:
#               data.loc[i,"FLB"]=0.00
#           else:
#               if (data.loc[i,"BLB"]>data.loc[i-1,"FLB"])|(data.loc[i-1,"Close"]<data.loc[i-1,"FLB"]):
#                   data.loc[i,"FLB"]=data.loc[i,"BLB"]
#               else:
#                   data.loc[i,"FLB"]=data.loc[i-1,"FLB"]



#       # SUPERTREND = IF((Previous SUPERTREND = Previous FINAL UPPERBAND) and (Current Close <= Current FINAL UPPERBAND)) THEN
#       #                 Current FINAL UPPERBAND
#       #             ELSE
#       #                 IF((Previous SUPERTREND = Previous FINAL UPPERBAND) and (Current Close > Current FINAL UPPERBAND)) THEN
#       #                     Current FINAL LOWERBAND
#       #                 ELSE
#       #                     IF((Previous SUPERTREND = Previous FINAL LOWERBAND) and (Current Close >= Current FINAL LOWERBAND)) THEN
#       #                         Current FINAL LOWERBAND
#       #                     ELSE
#       #                         IF((Previous SUPERTREND = Previous FINAL LOWERBAND) and (Current Close < Current FINAL LOWERBAND)) THEN
#       #                             Current FINAL UPPERBAND


#       for i, row in data.iterrows():
#           if i==0:
#               data.loc[i,"ST"]=0.00
#           elif (data.loc[i-1,"ST"]==data.loc[i-1,"FUB"]) & (data.loc[i,"Close"]<=data.loc[i,"FUB"]):
#               data.loc[i,"ST"]=data.loc[i,"FUB"]
#           elif (data.loc[i-1,"ST"]==data.loc[i-1,"FUB"])&(data.loc[i,"Close"]>data.loc[i,"FUB"]):
#               data.loc[i,"ST"]=data.loc[i,"FLB"]
#           elif (data.loc[i-1,"ST"]==data.loc[i-1,"FLB"])&(data.loc[i,"Close"]>=data.loc[i,"FLB"]):
#               data.loc[i,"ST"]=data.loc[i,"FLB"]
#           elif (data.loc[i-1,"ST"]==data.loc[i-1,"FLB"])&(data.loc[i,"Close"]<data.loc[i,"FLB"]):
#               data.loc[i,"ST"]=data.loc[i,"FUB"]

#       data.to_csv(symbol+'.csv',index=False)
#       print(data.tail(5))
#   except Exception:
#       None    


        
