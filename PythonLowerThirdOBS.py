# -*- coding: utf-8 -*-
"""
Created on Wed May 10 14:58:41 2023

@author: Afrin
"""

from tkinter import *


class GUI(Tk):
    
    def __init__(self, title_, bg_, geometry_, label_=None, btn=None, text_=None):
        Tk.__init__(self)
        self.title(title_)
        self.geometry(geometry_)      
        self.configure(background=bg_)
       
        if (label_ != None):
            self.lower_third_label =  Label(self, text='', font=('Arial', 30), relief='flat')
            self.lower_third_label.pack()
            
        if (text_ != None):
            self.lower_third_text = Entry(self)
            self.lower_third_text.pack()
            
        if (btn != None):
            self.control_gui_button = Button(self, text="Show Me", command=show_me)
            self.control_gui_button.pack()
                             
        
    def close_window(self, *args):
        """ Closes the GUI window."""
        del args
        self.destroy()
        
        
    

def show_me():    
    LowerThirdGUI.lower_third_label['text'] = ControlGUI.lower_third_text.get()



if __name__ == "__main__":
    ControlGUI = GUI('Control', 'blue', '800x100', btn=True, text_=True)
    LowerThirdGUI = GUI('Lower Thirds', 'green', '200x200', label_=True)


    ControlGUI.mainloop()
    LowerThirdGUI.mainloop()

