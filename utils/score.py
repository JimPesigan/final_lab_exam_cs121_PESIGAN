import datetime
from .user_manager import *

class Score:
	def __init__(self, filename='scores.txt'):
		self.filename = filename
		self.scores = {}
		self.wins = {}
