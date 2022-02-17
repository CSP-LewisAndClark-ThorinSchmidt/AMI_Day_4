# main.py
# gabe M / Maddie
# 02/01/22

'''
My Awesome App

Simple program to demonstrate how to create a login screen and switch frames in a single app.
'''

import tkinter as tk
import sys
from app import Application
from login import Login
#from login import Login

class Root(tk.Tk):
  """Root class"""

  def __init__(self):
    super(Root, self).__init__()
    self.title("My Awesome App")
    self.geometry("300x300")

  def change_to_app(self):
    app_frame.pack(fill = 'both', expand = 1)
    login_frame.forget()

  def login_pack():
    self.Login.pack()
  
  
  def login_fail(self):
    sys.exit()
  
# main
# The frames are called login_frame, and app_frame
# I'm pretty sure you can figure out which is which
# Check the announcements channel for linksto helpful
# resources.

#initlizing that root = root class
root = Root()
login = Login(root)
login.pack()
root.mainloop()