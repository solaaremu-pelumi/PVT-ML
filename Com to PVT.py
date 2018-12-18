# -*- coding: utf-8 -*-
"""
Created on Mon Dec 17 18:30:31 2018

@author: Pelumi
"""

"""This is the input page for Composition properties to PVT page"""

import tkinter as tk
from tkinter import ttk

class my_frame(tk.Frame):
    """This frame binds all that is required to be displayed"""
    
    def __init__(self,parent,*args,**kwargs):
        super().__init__(parent,*args,**kwargs)
        
        #Widget to be added
        predictor=['C1','C2','C3', 'IC4', 'NC4','IC5', 'NC5', 'C6','C7+','C02', 'N2','MW','MW(C7+)']
        for item in predictor:
            count=0
            item=ttk.Label(self,text=item+':')
            item.grid(row=count,column=0)
            count+=1
            
class my_application(tk.Tk):
    """Login main applicatin"""
    
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        
        self.title("PVT ML")
        self.resizable(width=False,height=False)
        
        #Defining the UI
        my_frame(self).grid(sticky=tk.W+tk.S+tk.E+tk.N)
        
if __name__ == "__main__":
    app=my_application()
    app.mainloop()
            
        