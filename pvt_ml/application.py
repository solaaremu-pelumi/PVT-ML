import tkinter as tk
from tkinter import ttk
from datetime import datetime
from . import comtopvt as c
from . import trainingcode as t

class my_application(tk.Tk):
    """XPVT ML"""
    
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        
        self.title("PVT ML")
        self.geometry("400x300")
        self.resizable(width=False,height=True)

        #Defining the UI
        self.cruise=c.CompositionInput(self)
        self.cruise.grid(row=0, padx=10)
        
        self.predict=ttk.Button(self,text="Predict",command=self.on_predict)
        self.predict.grid(row=1,sticky=(tk.W+tk.E))
        
    def on_predict(self):
        data=self.cruise.get()
        select=self.cruise.gett()
        reservoir=t.Reservoir()
        reservoir.data=data
        reservoir.select=select
        reservoir.bub_point_train()
        self.cruise.reset()
        return
