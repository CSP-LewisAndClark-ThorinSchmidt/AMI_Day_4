# login.py
# Dominic Thomeczek, Justin Clark
# 2/17/22

'''
Login Class File

A simple login frame that is displayed first. If the correct password is entered (It has been set to Pa$$word for this example), the program will switch to the Application frame.

BONUS: If the number of attempts exceeds 3, the program will exit.
'''

import tkinter as tk
import sys

class Login(tk.Frame):
    """ A GUI login frame with a label, entry box, and login button """

    def __init__(self, master):
        """ Initialize the Frame. """
        self.attempts = 0
        self.password = "Pa$$word"
        self.master = master

        super(Login, self).__init__(self.master)

        self._create_widgets()


    def _create_widgets(self):
        ''' Instantiate all widgets for the login class'''
        self.label_1 = tk.Label(self, text = 'Password')
        self.entry_1 = tk.Entry(self, width=10)

        self.entry_1.pack()
        self.label_1.pack()

        tk.Button(self, text='login', command=self.login_command).pack()

    def login_command(self):
        ''' return a bool of the login attempt '''
        self.text = self.entry_1.get()
        self.login = self.check_input()

    def check_input(self):
        ''' Check the user input is correct'''
        if self.attempts > 2:
          print("You failed! Goodbye!")
          self.master.login_fail()

        if self.attempts < 3 and self.text == self.password:
            self.master.change_to_app()
        elif self.text != self.password:
            self.attempts += 1
            print(f"You have {3 - self.attempts} attempts remaining!!!")
