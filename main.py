# main.py
# Josh Lyell, Andrew Vester
# 02/17/22

'''
My Awesome App

Simple program to demonstrate how to create a login screen and switch frames in a single app.
'''

import tkinter as tk
import sys
from app import Application
from login import Login


class Root(tk.Tk):
  """Root class"""

  def __init__(self):
    super(Root, self).__init__()
    self.geometry("300x300")
    self.title("My Awesome App")

  def change_to_app(self):
    app_frame.pack(fill = 'both', expand = 1)
    login_frame.forget()
  
  def login_fail(self):
    sys.exit()
  
# main
root = Root()

app_frame = Application(root)
login_frame = Login(root)

login_frame.pack(fill = 'both', expand = 1)

root.mainloop()