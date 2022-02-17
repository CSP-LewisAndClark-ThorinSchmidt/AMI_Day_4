# main.py
# Stephen Gantz and Gabriel Whitten
# 02/01/22

'''
My Awesome App

Simple program to demonstrate how to create a login screen and switch frames in a single app.
'''

import tkinter as tk
from tkinter import *
import sys
from app import Application
from login import Login

class Root(tk.Tk):
  """Root class"""
  def __init__(self):
    super(Root, self).__init__()
    self.title("My Awesome App")
    self.geometry("800x450")

  def change_to_app(self):
    app_frame.pack(fill = 'both', expand = 1)
    login_frame.forget()


  def login_fail(self):
    sys.exit()

# main

root = Root()
frame = Login(root)
frame.pack()
root.mainloop()
  
# The frames are called login_frame, and app_frame
# I'm pretty sure you can figure out which is which
# Check the announcements channel for linksto helpful
# resources.