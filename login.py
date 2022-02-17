# login.py
# Austin Klemme and Gavin Sutherland
# 02/17/22

'''
Login Class File 

A simple login frame that is displayed first. If the correct password is entered (It has been set to Pa$$word for this example), the program will switch to the Application frame.

BONUS: If the number of attempts exceeds 3, the program will exit. 
'''
import tkinter as tk

class Login(tk.Frame):
  """ A GUI login frame with a label, entry box, and login button """

  def __init__(self, master):
    """Initialize the Frame."""  
    super(Login, self).__init__(master)

    self.master = master
    self.create_widgets()

  def create_widgets(self):
    '''Creates the widgets'''
    self.lblOne = tk.Label(self, text = "Enter the Password")
    self.lblOne.pack()
    self.entry1 = tk.Entry(self)
    self.entry1.pack()
    self.btnOne = tk.Button(self, text = "Login", command =  self.check_pass)
    self.btnOne.pack()

  def check_pass(self):
    '''Checks if the password is correct'''
    pass_ent = self.entry1.get()
    if pass_ent == "pa$$word":
      self.master.change_to_app()

    else:
      self.master.login_fail()