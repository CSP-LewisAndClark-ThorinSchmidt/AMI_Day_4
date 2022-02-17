# login.py
# gabe M / Maddie
# //22

import tkinter as tk
import sys
from tkinter import *
from app import Application

'''
Login Class File 

A simple login frame that is displayed first. If the correct password is entered (It has been set to Pa$$word for this example), the program will switch to the Application frame.

BONUS: If the number of attempts exceeds 3, the program will exit. 
'''


class Login(tk.Frame):
    def __init__(self,master):
        super(Login, self).__init__() #thank you alex  for showing me this line 
        
        #This is the parent window so we will use master to show that
        self.master = master
        #make an entry field with char limit of 25 and packs it to make it visible.
        self.enter_your_password = Entry(self, width=25)
        self.enter_your_password.pack()
        #creates button and when it is pressed goes to the ' button_attempts ' function. to see if the password is correct or not. 
        self.try_login = Button(self, text="sign in", command = self.button_attempts)
        self.try_login.pack()


    def button_attempts(self):
      #checks if passowrd is equal to the correct password
      if (self.enter_your_password.get() == 'Pa$$word'):
        #added a bit of console logging for better user experience
        print("Correct")
        Application(self.master).pack()
        self.forget()
        #checks if password is not equal to teh correct password and prints a statement if not.
      if (self.enter_your_password.get() != 'Pa$$word'):
        print("incorrect try again")








