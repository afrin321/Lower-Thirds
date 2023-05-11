# -*- coding: utf-8 -*-
"""
Created on Wed May 10 14:58:41 2023

@author: Afrin
"""

from tkinter import *
from fs import *

class OperateGUI(object):
    
    @staticmethod
    def initialize(gui_, title_, bg_, geometry_):
        gui = gui_
        gui.title(title_)
        gui.geometry(geometry_)      
        gui.configure(background=bg_)
        
        return gui
    
    @staticmethod
    def set_button(gui_, text_, command_):
        button = Button(gui_, text=text_, command=command_)        
        return button
    
    @staticmethod
    def set_input(gui_):   
        return Entry(gui_)
    
    @staticmethod
    def set_label(gui_):   
        return Label(gui_, text='', font=('Arial', 30), relief='flat')
    
    @staticmethod
    def set_text():   
        show_me()
        
    @staticmethod
    def set_listbox(gui_):   
        return Listbox(gui_, width=75)
    
    @staticmethod
    def show_list_item(gui_):   
        i = gui_.listbox.curselection()[0]
        item = gui_.listbox.get(i)
        show_list_item(item)
        
    @staticmethod
    def read_file():  
        clear_all()
        f = open("lowerThirds3.txt", "r")
        past_lower_thirds = f.read()
        f.close()
        return past_lower_thirds.split(',')
    
    @staticmethod
    def clear_all():  
        clear_all()
    

        
        
        


class ControlGUI(Tk):
    
    def __init__(self, title_, bg_, geometry_):
        Tk.__init__(self)
        OperateGUI.initialize(self, title_, bg_, geometry_)
        
        self.lower_third_text = OperateGUI.set_input(self)
        self.lower_third_text.pack()
        
        self.control_gui_button = OperateGUI.set_button(self, 'Show Me', OperateGUI.set_text)
        self.control_gui_button.pack()
        
        self.reset_button = OperateGUI.set_button(self, "Reset", OperateGUI.clear_all)
        self.reset_button.pack()
        
        self.listbox = OperateGUI.set_listbox(self)
        self.listbox.pack()
        self.listbox.bind('<<ListboxSelect>>', self.on_select_list)
        
        self.load_button = OperateGUI.set_button(self, 'Load', self.load)
        self.load_button.pack(anchor='n', side='right')
        
               
    
    def on_select_list(self, e):
       OperateGUI.show_list_item(self)
        
    def load(self):
       
        temp_list = OperateGUI.read_file()        
        
        for l in temp_list:
            self.listbox.insert(END, l.strip('\n'))
        
    def clear(self):
        self.listbox.delete(0,END)
        self.lower_third_text.delete(0, END)
        
        


class LowerThirdGUI(Tk):
    
    def __init__(self, title_, bg_, geometry_):
        Tk.__init__(self)
        OperateGUI.initialize(self, title_, bg_, geometry_)
        
        self.lower_third_label =  OperateGUI.set_label(self)
        self.lower_third_label.pack()
        
    def clear(self):
        self.lower_third_label['text'] = ''
        
    



if __name__ == "__main__":
    ControlGUI = ControlGUI('Control', 'blue', '800x100')
    LowerThirdGUI = LowerThirdGUI('Lower Thirds', 'green', '200x200')
    
    def show_me():    
        LowerThirdGUI.lower_third_label['text'] = ControlGUI.lower_third_text.get()
        
        
    def show_list_item(text_):
        LowerThirdGUI.lower_third_label['text'] = text_
        
    def clear_all():
        LowerThirdGUI.clear()
        ControlGUI.clear()


    ControlGUI.mainloop()
    LowerThirdGUI.mainloop()

