# login.py
# Josh Lyell, Andrew Vester
# 2/17/22

'''
Login Class File 

A simple login frame that is displayed first. If the correct password is entered (It has been set to Pa$$word for this example), the program will switch to the Application frame.

BONUS: If the number of attempts exceeds 3, the program will exit. 
'''
import tkinter as tk

class Login(tk.Frame):
  """ A GUI login frame with a label, entry box, and login button """

  def __init__(self, master):
    """ Initialize the Frame. """
    
    super(Login, self).__init__(master)
    
    self.master = master
    self.create_widgets()

  def create_widgets(self):
    """ Create a label, and a button that changes the frame. """
    
    self.label1 = tk.Label(self, text = "Enter the password")
    self.label1.pack()
    
    self.entry1 = tk.Entry(self, width = 20)
    self.entry1.pack()

    self.button1 = tk.Button(self, text="Login",
                            command=self.button_command)
    self.button1.pack()

  def button_command(self):
    text = self.entry1.get()
    if text == "Pa$$word":
      self.master.change_to_app()