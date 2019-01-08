import tkinter as tk
from tkinter import ttk
from datetime import datetime
import os
import csv
from decimal import Decimal, InvalidOperation 

class ValidatedMixin:
    """Adds a validation functionality to an input widget"""
    def __init__(self,*arg,error_var=None,**kwargs):
        self.error=error_var or tk.StringVar()
        super().__init__(*arg,**kwargs)

        vcmd=self.register(self._validate)
        invcmd=self.register(self._invalid)

        self.config(validate='all',validatecommand=(vcmd,'%P','%s','%S','%V','%i','%d'),invalidcommand=(invcmd,'%P','%s','%S','%V','%i','%d'))

    def _toggle_error(self, on=False):
        self.config(foreground=('red' if on else 'black'))

    def _validate(self,proposed,current,char,event,index,action):
        self._toggle_error(False)
        self.error.set('')
        valid=True
        if event =='focusout':
            valid=self._focusout_validate(event=event)
        elif event =='key':
            valid=self._key_validate(proposed=proposed, current=current,char=char,event=event, index=index, action=action)
        return valid
    
    def _focusout_validate(self,**kwargs):
        return True

    def _key_validate(self,**kwargs):
        return True
    
    def _invalid(self,proposed,current,char,event,index,action):
        if event =='focusout':
            self._focusout_invalid(event=event)
        elif event =='key':
            self._key_invalid(proposed=proposed, current=current,char=char,event=event, index=index, action=action)
    
    def _focusout_invalid(self,**kwargs):
        self._toggle_error(True)

    def _key_invalid(self,**kwargs):
        pass    

    def trigger_focusout_validation(self):
        valid=self._validate("","","","focusout","","")
        if not valid:
            self._focusout_invalid(event='focusout')
        return valid

class ValidatedSpinbox(ValidatedMixin,tk.Spinbox):
    
    def __init__(self,*args,min_var=None,max_var=None,focus_update_var=None,from_='Infinity',to='Infinity',**kwargs):
        super().__init__(*args,from_=from_,to=to,**kwargs)
        self.resolution=Decimal(str(kwargs.get('increment','1.0')))
        self.precision=(self.resolution.normalize().as_tuple().exponent)

    def _key_validate(self,char,index,current,proposed,action,**kwargs):
        valid=True
        min_val=self.cget('from')
        max_val=self.cget('to')
        no_negative=min_val>=0
        no_decimal=self.precision >= 0
        if action =='0':
            return True
        #First, filter out obviously invalid keystrokes
        if any([(char not in('-1234567890.')),(char =='-' and (no_negative or index!='0')),(char=='.' and (no_decimal or '.' in current))]):
            return False

        #At this point, proposed is either '-','.','-.', or a valid Decimal String
        if proposed in '-.':
            return True
        #Proposed is a valid Decimal String convert to Decimal and Check more:
        proposed = Decimal(proposed)
        proposed_precision=proposed.as_tuple().exponent

        if any([(proposed>max_val),(proposed_precision<self.precision)]):
            return False

        return valid
    def _focusout_validate(self,**kwargs):
        valid=True
        value=self.get()
        min_val=self.cget('from')

        try:
            value=Decimal(value)
        except InvalidOperation:
            self.error.set('Invalid number string: {}'.format(value))
            return False
        
        if value<min_val:
            self.error.set('Value is too low(min {})'.format(min_val))
            valid =False
        return valid

class LabelInput(tk.Frame):
    """A widget containing a label and input together"""
    
    def __init__(self,parent,label="",input_class=ValidatedSpinbox,input_var=None,input_args=None,label_args=None,**kwargs):
        super().__init__(parent,**kwargs)
        input_args=input_args or {}
        label_args=label_args or {}
        self.variable=input_var
        
        if input_class in (ttk.Checkbutton,ttk.Button,ttk.Radiobutton):
            input_args["text"]=label
            input_args["variable"]=input_var
        else:
            self.label=ttk.Label(self,text=label,**label_args)
            self.label.grid(row=0,column=0,sticky=(tk.W+tk.E))
            input_args["textvariable"]=input_var
            
        self.input= input_class(self,**input_args)
        self.input.grid(row=0,column=1,sticky=(tk.W+tk.E))
        self.columnconfigure(0,weight=1)
            
    def grid(self,sticky=(tk.E+tk.W),**kwargs):
        super().grid(sticky=sticky,**kwargs)
    
    def get(self):
        try:
            if self.variable:
                return self.variable.get()
            elif type(self.input) == tk.Text:
                return self.input.get('1.0',tk.END)
            else:
                return self.input.get()
        except (TypeError, tk.TclError):
            # happens when numeric firelds are empty.
            return ''
    
    def set(self,value,*args,**kwargs):
        if type(self.variable) == tk.BooleanVar:
            self.variable.set(bool(value))
        elif self.variable:
            self.variable.set(value,*args,**kwargs)
        elif type(self.input) in (ttk.Checkbutton, ttk.Radiobutton):
            if value:
                self.input.select()
            else:
                self.input.deselect()
        elif type(self.input) == tk.Text:
            self.input.delete('1.0',tk.END)
            self.input.insert('1.0',value)
        else: #input must be an Entry-type widget with no variable
            self.input.delete(0,tk.END)
            self.input.insert(0,value)