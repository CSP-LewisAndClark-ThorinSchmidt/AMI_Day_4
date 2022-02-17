# login.py
# 
# //22

import tkinter as tk
from tkinter import *
from app import Application


class Login(tk.Frame):
  """ A GUI login frame with a label, entry box, and login button """

  login_tries = 0

  def __init__(self, master):
    """ Initialize the Frame. """
    super(Login, self).__init__()
    self.master = master
    self.passwordEntry = Entry(self, width=50)
    self.loginButton = Button(self, text="Enter Your Password", command = self.button_callback)
    self.passwordEntry.pack()
    self.loginButton.pack()

  def button_callback(self):
    self.login_tries += 1

    if self.login_tries > 3:
      exit()

    if (self.passwordEntry.get() == "Pa$$word"):
      self.destroy()
      app = Application(self.master)
      app.pack()