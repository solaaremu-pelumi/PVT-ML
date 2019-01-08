# -*- coding: utf-8 -*-
"""
Created on Mon Dec 17 18:30:31 2018

@author: Pelumi
"""

"""This is the input page for Composition properties to PVT page"""

import tkinter as tk
from tkinter import ttk
from datetime import datetime
import os
import csv
from decimal import Decimal, InvalidOperation       
from . import widgets as w

class SelectionInput(tk.Frame):
    """This class serves as the selection input class for the label frame"""
    def __init__(self,parent,*args,**kwargs):
        super().__init__(parent,*args,**kwargs)
        #A dict to keep track of selection widgets.
        self.selection={}
        predict_choice=tk.LabelFrame(self,text="Selection")
        predict_desc=ttk.Label(predict_choice, text="PVT Properties to be predicted")
        predict_desc.grid(row=0,column=0,columnspan=2,sticky=tk.W)
        self.selection["bub_point"]=w.LabelInput(predict_choice,label="Bubble Point",input_class=ttk.Checkbutton,input_var=tk.BooleanVar())
        self.selection["bub_point"].grid(row=1,column=0)
        self.selection["sol_ratio"]=w.LabelInput(predict_choice,label="Solution Gas Oil Ratio",input_class=ttk.Checkbutton,input_var=tk.BooleanVar())
        self.selection["sol_ratio"].grid(row=1,column=1)
        self.selection["oil_visc"]=w.LabelInput(predict_choice,input_class=ttk.Checkbutton,label="Oil Viscosity",input_var=tk.BooleanVar())
        self.selection["oil_visc"].grid(row=2,column=0)
        self.selection["fvf"]=w.LabelInput(predict_choice,input_class=ttk.Checkbutton,label="Formation Volume Factor",input_var=tk.BooleanVar())
        self.selection["fvf"].grid(row=2,column=1)
        predict_choice.grid(row=0,column=0)
    
    def get(self):
        select={}
        for key,widget in self.selection.items():
            select[key]=widget.get()
        return select

    def reset(self):
        for widget in self.selection.values():
            widget.set('')

class CompositionInput(tk.Frame):
    """The input for our widgets"""
    
    def __init__(self,parent,*args,**kwargs):
        super().__init__(parent, *args,**kwargs)
        #A dict to keep track of input widgets
        self.inputs={}
        
        composition=tk.LabelFrame(self,text="Composition")
        
        self.inputs["C1"]=w.LabelInput(composition,label="C1",input_args={"from_":0.00,"to":100.0,"increment":0.01},input_var=tk.DoubleVar())
        self.inputs['C1'].grid(row=0,column=0)
        self.inputs["C2"]=w.LabelInput(composition,label="C2",input_args={"from_":0.00,"to":100.0,"increment":0.01},input_var=tk.DoubleVar())
        self.inputs["C2"].grid(row=1,column=0)
        self.inputs["C3"]=w.LabelInput(composition,label="C3",input_args={"from_":0.00,"to":100.0,"increment":0.01},input_var=tk.DoubleVar())
        self.inputs["C3"].grid(row=2,column=0)
        self.inputs["IC4"]=w.LabelInput(composition,label="IC4",input_args={"from_":0.00,"to":100.0,"increment":0.01},input_var=tk.DoubleVar())
        self.inputs["IC4"].grid(row=3,column=0)
        self.inputs["NC4"]=w.LabelInput(composition,label="NC4",input_args={"from_":0.00,"to":100.0,"increment":0.01},input_var=tk.DoubleVar())
        self.inputs["NC4"].grid(row=4,column=0)
        self.inputs["IC5"]=w.LabelInput(composition,label="IC5",input_args={"from_":0.00,"to":100.0,"increment":0.01},input_var=tk.DoubleVar())
        self.inputs["IC5"].grid(row=5,column=0)
        self.inputs["NC5"]=w.LabelInput(composition,label="NC5",input_args={"from_":0.00,"to":100.0,"increment":0.01},input_var=tk.DoubleVar())
        self.inputs["NC5"].grid(row=6,column=0)
        self.inputs["C6"]=w.LabelInput(composition,label="C6",input_args={"from_":0.00,"to":100.0,"increment":0.01},input_var=tk.DoubleVar())
        self.inputs["C6"].grid(row=7,column=0)
        self.inputs["C7+"]=w.LabelInput(composition,label="C7+",input_args={"from_":0.00,"to":100.0,"increment":0.01},input_var=tk.DoubleVar())
        self.inputs["C7+"].grid(row=8,column=0)
        self.inputs["CO2"]=w.LabelInput(composition,label="CO2",input_args={"from_":0.00,"to":100.0,"increment":0.01},input_var=tk.DoubleVar())
        self.inputs["CO2"].grid(row=9,column=0)
        self.inputs["N2"]=w.LabelInput(composition,label="N2",input_args={"from_":0.00,"to":100.0,"increment":0.01},input_var=tk.DoubleVar())
        self.inputs["N2"].grid(row=10,column=0)
        self.inputs["MW"]=w.LabelInput(composition,label="MW",input_args={"from_":0.00,"to":500.0,"increment":0.01},input_var=tk.DoubleVar())
        self.inputs["MW"].grid(row=11,column=0)
        self.inputs["MW(C7+)"]=w.LabelInput(composition,label="MW(C7+)",input_args={"from_":0.00,"to":500.0,"increment":0.01},input_var=tk.DoubleVar())
        self.inputs["MW(C7+)"].grid(row=12,column=0)
        composition.grid(row=0,column=0)
        self.reset()

    def get(self):
        data={}
        for key,widget in self.inputs.items():
            data[key]=widget.get()
        return data

    def reset(self):
        for widget in self.inputs.values():
            widget.set('')

class ResultOutput(tk.Frame):
    """This class presents the results from the machine learning model"""
    def __init__(self,parent,*args,**kwargs):
        super().__init__(parent,*args,*kwargs)
        #A dictionary to keep the results widget
        self.result={}
        results=ttk.LabelFrame(self,text="Result")
        bubble_point=w.LabelInput(results,label="Pb psi",input_class=ttk.Label,input_var=tk.StringVar())
        bubble_point.grid(row=0,column=0)
        results.grid(row=0,column=0)
