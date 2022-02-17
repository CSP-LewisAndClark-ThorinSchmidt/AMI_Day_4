
import tkinter as tk
from tkinter import *
from app import Application

'''
Login Class File 

A simple login frame that is displayed first. If the correct password is entered (It has been set to Pa$$word for this example), the program will switch to the Application frame.

BONUS: If the number of attempts exceeds 3, the program will exit. 
'''

class Login(tk.Frame):
  """ A GUI login frame with a label, entry box, and login button """

  attempts = 0

  def __init__(self, master):
    """ Initialize the Frame. """
    super(Login, self).__init__()
    self.master = master
    self.usernameEntry = Entry(self, width=20)
    self.passwordEntry = Entry(self, width=20)
    self.loginButton = Button(self, text="Log in", command = self.button_callback)
    self.usernameEntry.pack()
    self.passwordEntry.pack()
    self.loginButton.pack()

  def button_callback(self):
    self.attempts += 1

    if self.attempts > 3:
      exit(0)

    if (self.passwordEntry.get() == "Pa$$word"):
      self.destroy()
      app = Application(self.master)
      app.pack()





