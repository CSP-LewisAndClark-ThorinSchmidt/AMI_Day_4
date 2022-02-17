# login.py
# Jackson VanderPloeg & Kaden Roof
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
		""" Initialize the Frame. """

		super(Login, self).__init__(master)
		self.master = master
		self.create_widgets()
		self.password = 'Pa$$word'
		self.attempts = 0

	def button_command(self):
		if self.entry1.get() == self.password:
			self.master.change_to_app()
		else:
			self.attempts += 1
		if self.attempts >= 3:
			self.master.login_fail()

	def create_widgets(self):
		""" Create a label, and a button that exits. """

    # create the label
		msg = "Enter the password"
		self.lblOne = tk.Label(self, text = msg)
		self.lblOne.pack()

		self.entry1 = tk.Entry(self, width = 20)
		self.entry1.pack()

		self.btnLogin = tk.Button(self, text = "Login", 
                                command= self.button_command)
		self.btnLogin.pack()



