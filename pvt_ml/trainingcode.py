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

class Reservoir():
    """This class represents the instance of a particular reservoir, having the properties of composition and being able to predict the execution of reservoir pvt properties"""

    predictor=['C1','C2','C3', 'IC4', 'NC4','IC5', 'NC5', 'C6','C7+','C02', 'N2','MW','MW(C7+)']
    response=['FIELD', 'WELL ', 'RESERVOIR', 'Depth ft_ss', 'Pressure psi', 'PB psi', 'RSI scf/bbl', 'Boi v/v', 'SG Oil', 'Oil Visc cp', 'GOR scf/bbl', 'Oil 60/60f','Gas air=1','Temp deg.F']
    df=pd.read_csv('D:\\Users\\Pelumi\\Pelumi\\Petroleum Engineering\\Projects\\TPE 599\\Code\\Data\\PVT RSI Data.csv')
    npdc=pd.read_csv('D:\\Users\\Pelumi\\Pelumi\\Petroleum Engineering\\Projects\\TPE 599\\Code\\Data\\NPDC PVT Data.csv')

    def __init__(self,data=None,select=None,frame=None,*args,**kwargs):
        self.data=data
        self.select=select
        self.result={}
        
    def bub_point_pre_process(self):
        if self.select["PB psi"]!=True:
            pass
        else:
            self.frame_bub=self.pre_process(action=self.npdc,element="PB psi")
            return self.frame_bub
        
    def bub_point_train(self):
        try:
            self.frame_bub=self.bub_point_pre_process()
            framex_train, framex_test, framey_train, framey_test=tts((self.frame_bub.iloc[:,:-1]),self.frame_bub.iloc[:,-1],test_size=0.2, random_state=123)
            model=ElasticNet()
            model.fit(framex_train,framey_train)
            value= np.fromiter(self.data.values(), dtype=float).reshape(1,13)
            print(model.predict(value))
        except:
            pass
   
    def pre_process(self,action,element):
        x=[]
        frame=action.copy(deep=True)
        for row in action:
            x.append(row)
        for item in x:
            if item==element:
                pass
            elif item in self.response:
                frame.drop(item,axis=1,inplace=True)
        return frame