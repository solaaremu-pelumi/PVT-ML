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
        self.selection=c.SelectionInput(self)
        self.selection.grid(row=0,column=0)
        self.compose=c.CompositionInput(self)
        self.compose.grid(row=1,padx=10)
        self.result=c.ResultOutput(self)
        self.result.grid(row=3,column=0)
        self.predict=ttk.Button(self,text="Predict",command=self.on_predict)
        self.predict.grid(row=2,sticky=(tk.W+tk.E))

        
    def on_predict(self):
        data=self.compose.get()
        select=self.selection.get()
        reservoir=t.Reservoir(data=data,select=select)
        reservoir.bub_point_train()
        reservoir.form_fact_train()
        reservoir.sol_gas_rat_train()
        self.compose.reset()
        self.selection.reset()
        return
