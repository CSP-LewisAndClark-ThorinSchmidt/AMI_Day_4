# !/usr/binenv python3
# Jeff Kimani
# 2/17/2022
# login.py

#Partner Jacob Smith

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
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        """ Create a label, and a button that changes the frame. """
    
        # create the label
        msg = "Welcome to Frame 1!"
        self.lblOne = tk.Label(self, text = msg)
        self.lblOne.pack()
        self.btnOne = tk.Button(self, text = "Go to Frame 2", command = self.master.change_to_2)
        self.btnOne.pack()
        #self.entry1 = Entry(self, width=20).pack()
        










