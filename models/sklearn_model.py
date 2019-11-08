import pandas as pd
import datetime
import pandas_datareader.data as web
from pandas import Series, DataFrame
import math
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.neighbors import KNeighborsRegressor

from sklearn.linear_model import Ridge
from sklearn.preprocessing import PolynomialFeatures
from sklearn.pipeline import make_pipeline 
import sklearn.preprocessing
from sklearn.model_selection import train_test_split
from sklearn import tree

data = []
period = []
close = []


for year in range(2017, 2019):
    for month in range(1,13):
        for day in range(1,32):
            try:
                start = datetime.date(year, month, day)
                end = datetime.date((year + 1), month, day)
            
                print(f' From period: {start} to {end}')
        
                #get stock Data
                df = web.DataReader("NFLX", 'yahoo', start, end)

                #Convert Data
                dfreg = df.loc[:,['Adj Close','Volume']]
                dfreg['HL_PCT'] = (df['High'] - df['Low']) / df['Close'] * 100.0
                dfreg['PCT_change'] = (df['Close'] - df['Open']) / df['Open'] * 100.0

                # Drop missing value
                dfreg.fillna(value=-99999, inplace=True)

                #select percednt of dtata for forecast into the future currently set to 5%
                forecast_out = int(math.ceil(0.05 * len(dfreg)))

                # Separating the label here, we want to predict the AdjClose
                forecast_col = 'Adj Close'
                dfreg['label'] = dfreg[forecast_col].shift(-forecast_out)
                X = np.array(dfreg.drop(['label'], 1))

                # Scale the X so that everyone can have the same distribution for linear regression
                X = sklearn.preprocessing.scale(X)

                # Finally We want to find Data Series of late X and early X (train) for model generation and evaluation
                X_lately = X[-forecast_out:]
                X = X[:-forecast_out]

                # Separate label and identify it as y
                y = np.array(dfreg['label'])
                y = y[:-forecast_out]

                #set training perameters
                X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=1)

                # Linear regression
                clfreg = LinearRegression(n_jobs=-1)
                clfreg.fit(X_train, y_train)

                # Quadratic Regression 2
                clfpoly2 = make_pipeline(PolynomialFeatures(2), Ridge())
                clfpoly2.fit(X_train, y_train)

                # Quadratic Regression 3
                clfpoly3 = make_pipeline(PolynomialFeatures(3), Ridge())
                clfpoly3.fit(X_train, y_train)

                # KNN Regression
                clfknn = KNeighborsRegressor(n_neighbors=2)
                clfknn.fit(X_train, y_train)

                confidencereg = clfreg.score(X_test, y_test)
                confidencepoly2 = clfpoly2.score(X_test,y_test)
                confidencepoly3 = clfpoly3.score(X_test,y_test)
                confidenceknn = clfknn.score(X_test, y_test)

                # print(confidencereg)
                # print(confidencepoly2)
                # print(confidencepoly3)
                # print(confidenceknn)

                #perfrom forecasting
                forecast_set = clfpoly3.predict(X_lately)
                dfreg['Forecast'] = np.nan
                df_close = df['Close'].iloc[-1]

                data.append(forecast_set)
                period.append(end)
                close.append(df_close)
                
            except:
                print("not valid date")


today = pd.DataFrame(data)
P_dates = pd.DataFrame(period)
closed = pd.DataFrame(close)

merged = P_dates.merge(today, left_index=True, right_index=True)
p_merged = merged.merge(closed, left_index=True, right_index=True)
semi_final = p_merged.rename(columns={'0_x': "date", 0: 'close_price','0_y': 'day_1_pred', 1: 'day_2_pred', 2: 'day_3_pred',3: 'day_4_pred',4: 'day_5_pred',5: 'day_6_pred',6: 'day_7_pred',7: 'day_8_pred',
                                8: 'day_9_pred',9: 'day_10_pred',10: 'day_11_pred',11: 'day_12_pred',12: 'day_13_pred'})

final = semi_final[['date', 'close_price', 'day_1_pred','day_2_pred', 'day_3_pred','day_4_pred','day_5_pred','day_6_pred','day_7_pred', 'day_8_pred',
                                'day_9_pred', 'day_10_pred', 'day_11_pred', 'day_12_pred', 'day_13_pred']]

final.to_csv("Data/poly3.csv")
