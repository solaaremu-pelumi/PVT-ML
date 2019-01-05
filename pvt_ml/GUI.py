"""This is the first page in the GUI of the app"""

import tkinter as tk
from tkinter import ttk

class my_frame(tk.Frame):
    """Frame to hold the design"""
    
    def __init__(self,parent,*args,**kwargs):
        super().__init__(parent,*args,**kwargs)
        
        #Widgetsgit 
        use_label=ttk.Label(self, text='Username:')
        pass_label=ttk.Label(self, text='Password:')
        use_entry=ttk.Entry(self)
        pass_entry=ttk.Entry(self,show='*')
        enter_button=ttk.Button(self,text="Log in")
        
        #Widget Layout
        use_label.grid(row=0,column=0,sticky=tk.W)
        use_entry.grid(row=0,column=1,sticky=tk.E)
        pass_label.grid(row=1,column=0,sticky=tk.W)
        pass_entry.grid(row=1,column=1,sticky=tk.E)
        enter_button.grid(row=2,column=1)

class my_application(tk.Tk):
    """Login main applicatin"""
    
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        
        self.title("PVT ML")
        self.geometry("220x100")
        self.resizable(width=False,height=False)
        
        #Defining the UI
        my_frame(self).grid(sticky=tk.W+tk.S+tk.E+tk.N)
        
if __name__ == "__main__":
    app=my_application()
    app.mainloop()
    
    
        
        
        