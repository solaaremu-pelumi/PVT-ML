# -*- coding: utf-8 -*-
"""
Created on Mon Dec  3 20:06:54 2018

@author: Pelumi
"""

"""This Program is used to develop empirical corelations for Niger Delta Crude"""
from yellowbrick.regressor import AlphaSelection
from yellowbrick.regressor import ResidualsPlot
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split as tts
from sklearn.metrics import mean_squared_error as mse
from sklearn.metrics import mean_absolute_error as mae
from sklearn.metrics import r2_score as r2
from sklearn.feature_selection import RFECV
from sklearn.linear_model import ElasticNetCV
from sklearn.linear_model import ElasticNet
from sklearn.preprocessing import PolynomialFeatures
from sklearn.feature_selection import RFECV
from scipy import math as mth


predictor=['C1','C2','C3', 'IC4', 'NC4','IC5', 'NC5', 'C6','C7+','C02', 'N2','MW','MW(C7+)']
response=['FIELD', 'WELL ', 'RESERVOIR', 'Depth ft_ss', 'Pressure psi', 'PB psi', 'RSI scf/bbl', 'Boi v/v', 'SG Oil', 'Oil Visc cp', 'GOR scf/bbl', 'Oil 60/60f','Gas air=1','Temp deg.F']

def import_file():
    """This function imports the training set file"""
    global df
    df=pd.read_csv('D:\\Users\\Pelumi\\Pelumi\\Petroleum Engineering\\Projects\\TPE 599\\Code\\Data\\PVT RSI Data.csv')
    return df

def import_file_NPDC():
    """This function imports the training set file for the NPDC Data"""
    global npdc
    npdc=pd.read_csv('D:\\Users\\Pelumi\\Pelumi\\Petroleum Engineering\\Projects\\TPE 599\\Code\\Data\\NPDC PVT Data.csv')
    return npdc

def plot_two_series(a,b):
    '''This function assists in plotting scatter plots'''
    plt.scatter(a,b)
    plt.title(a.name+" versus Bubble Point Pressure")
    plt.xlabel(a.name)
    plt.ylabel(b.name)
    plt.show
    
def predict_file(df,pred):
    """This function takes the dataset and drops all unrequired columns for prediction"""
    x=[]
    global frame
    frame=df.copy(deep=True)
    for row in df:
        x.append(row)
    for item in x:
        if item==pred:
            pass
        elif item in response:
            frame.drop(item,axis=1,inplace=True)
            
def split_data(df):
    global framex_train, framex_test, framey_train, framey_test
    framex_train, framex_test, framey_train, framey_test=tts((df.iloc[:,:-1]),df.iloc[:,-1],test_size=0.2, random_state=123)

def mean_absolute_percentage_error(y_true, y_pred): 
    return np.mean(np.abs((y_true - y_pred) / y_true)) * 100

def train_model(model):
    global framey_test_pred,framey_train_pred
    model=model()
    model.fit(framex_train,framey_train)
    framey_train_pred=model.predict(framex_train)
    framey_test_pred=model.predict(framex_test)
    RMSE_train=mse(framey_train,framey_train_pred)
    RMSE_test=mse(framey_test,framey_test_pred)
    MAE_train=mae(framey_train,framey_train_pred)
    MAE_test=mae(framey_test,framey_test_pred)
    R2_train=r2(framey_train,framey_train_pred)
    R2_test=r2(framey_test,framey_test_pred)
    MAPE_train=mean_absolute_percentage_error(framey_train,framey_train_pred)
    MAPE_test=mean_absolute_percentage_error(framey_test,framey_test_pred)
    print("The results of thefit for the trained dataset are as follows RMSE:%d, MAE:%d, R2:%d, MAPE:%d" %(RMSE_train,MAE_train,R2_train,MAPE_train))
    print("The results of the fit for the test dataset are as follows RMSE:%d, MAE:%d, R2:%dMAPE:%d" %(RMSE_test,MAE_test,R2_test,MAPE_test))
    print(model.coef_)
    print(model.intercept_)
    print(model.score(framex_train,framey_train))
    print(model.score(framex_test,framey_test))

import_file()
npdc=import_file_NPDC()
predict_file(npdc,'PB psi')
predict_file(df,'Oil Visc cp')
split_data(frame)
train_model(LinearRegression)
poly=PolynomialFeatures(2)
y=poly.fit_transform(framex_train)
z=poly.fit_transform(framex_test)


ECV=ElasticNet(alpha=15,max_iter=100000)
visualizer=AlphaSelection(ECV)
visualizer.fit(framex_train,framey_train)
visualizer.poof()
ECV.fit(framex_train,framey_train)
framey_test_pred=ECV.predict(framex_test)
framey_train_pred=ECV.predict(framex_train)
mean_absolute_percentage_error(framey_train, framey_train_pred)
mae(framey_train,framey_train_pred)
mean_absolute_percentage_error(framey_test, framey_test_pred)
mae(framey_test,framey_test_pred)

#Bo
#framey_train_run=np.log10(framey_train)
#framey_test_run=np.log10(framey_test)
#poly=PolynomialFeatures(2)
#y=poly.fit_transform(framex_train)
#z=poly.fit_transform(framex_test)
#ECV=ElasticNet(alpha=2.2,max_iter=100000)
#ECV.fit(y,framey_train_run)
#framey_train_pred_run=ECV.predict(y)
#framey_test_pred_run=ECV.predict(z)
#framey_train_pred=10**(framey_train_pred_run)
#framey_test_pred=10**(framey_test_pred_run)
#mean_absolute_percentage_error(framey_train, framey_train_pred)
#mae(framey_train,framey_train_pred)
#mean_absolute_percentage_error(framey_test, framey_test_pred)
#mae(framey_test,framey_test_pred)



##Pb
#npdc=import_file_NPDC()
#predict_file(npdc,'PB psi')
#split_data(frame)
#train_model(ElasticNet)
   

##RSI
#estimator=ECV
#selector=RFECV(estimator,step=1,cv=3)
#selector=selector.fit(y,framey_train)
#ECV=ElasticNet(alpha=350,max_iter=1000000)
#visualizer=AlphaSelection(ECV)
#visualizer.fit(y,framey_train)
#visualizer.poof()
#ECV.fit(y,framey_train)
#framey_test_pred=ECV.predict(z)
#framey_train_pred=ECV.predict(y)
#mean_absolute_percentage_error(framey_train, framey_train_pred)
#mae(framey_train,framey_train_pred)
#mean_absolute_percentage_error(framey_test, framey_test_pred)
#mae(framey_test,framey_test_pred)
#poly=PolynomialFeatures(2)
#y=poly.fit_transform(framex_train)
#z=poly.fit_transform(framex_test)
