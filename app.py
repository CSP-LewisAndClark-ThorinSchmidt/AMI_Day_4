# app.py
# gabe M / Maddie/ stolen from mr schmidt.
# 02/01/22

'''
App Class File 

A generic GUI window class to represent an app that
starts after a successful login. 
'''

import tkinter as tk
import sys

class Application(tk.Frame):
  """ A GUI application with a label and a button. """

  def __init__(self, master):
    """ Initialize the Frame. """
    
    super(Application, self).__init__(master)
    #self.grid() (this breaks things with pack, removed for the time being.)
    self.create_widgets()

  def create_widgets(self):
    """ Create a label, and a button that exits. """
    
    # create the label
    msg = "Welcome to your app!"
    self.lblOne = tk.Label(self, text = msg)
    self.lblOne.pack()
    self.btnExit = tk.Button(self, text = "Exit", 
                             command= sys.exit)
    self.btnExit.pack()
