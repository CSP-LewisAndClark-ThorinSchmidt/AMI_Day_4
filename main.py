# main.py
# Dominic Thomeczek, Justin Clark
# 2/17/22

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
    self.title("My Bad App")
    self.geometry("300x300")

  def change_to_app(self):
    app_frame.pack(fill = 'both', expand = 1)
    login_frame.forget()

  def login_fail(self):
    sys.exit()

# main
# The frames are called login_frame, and app_frame
# I'm pretty sure you can figure out which is which
# Check the announcements channel for linksto helpful
# resources.

root = Root()

login_frame = Login(root)
app_frame = Application(root)

login_frame.pack(fill = 'both', expand = 1)

root.mainloop()