from .dice_game import *
from .user import*
import os
game = DiceGame()

class UserManager:
	def __init__(self):
		self.accounts = {}
		
	def load_users(self):
		if not os.path.exists("users.txt"):
			with open('users.txt', 'w') as f:
				f.write("")
		  

	def save_users(self):
		with open('user.txt', 'w') as f:
			for account in self.accounts:
				f.write(f"{self.accounts[account].name},{self.accounts[account].password}\n")

	
	def register(self):
		while True:
			username = input("Enter username (atleast 4 characters), or leave blank to cancel: ")
			if username == "":
				return
			if username in self.accounts:
				print("Username already exists.")
				continue
			if len(username) < 4:
				print("Username must be atleast 4 characters long.")
				continue
			
			password = input("Enter password (at least 8 characters), or leave blank to cancel: ")
			if password == "":
				return self.register(username)
			if len(password) < 8:
				print("Password must be atleast 8 characters long.")
			
					
			self.accounts[username] = User(username, password)
			self.save_users()
			print("Registration Successful.")
			return
		
  
	def login(self):
		while True:	
			username = input("Enter username, or leave blank to cancel: ")
			password = input("Enter password, or leave blank to cancel: ")
			if len(username) ==  0:
				return
			if len(password) ==  0:
				return

			if self.accounts[username].password != password:
				print("Credentials are incorrect.")
				continue
			if username not in self.accounts[username]:
				print("Entered credentials are incorrect.")
				continue
			account = self.accounts[username]
			print(f"Login successful!")

			game.menu(self, username)
			return

			