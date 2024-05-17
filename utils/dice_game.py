import random
from .score import *

points = 0
wins = 0

class DiceGame:
	def __init__(self):
		self.score_manager = Score()

	def load_scores(self):
		self.score_manager.load_score()

	def save_scores(self):
		self.score_manager.save_score()

	def play_game(self, username):
		while True:
			if self.rolls(username) == True:
				choice = input("Do you want to continue to the next stage? (1 for Yes, 0 for No): ")
				if choice == 1:
					continue
				elif choice == 0:
					break
			else:
				self.menu(username)

	def show_top_scores(self):
		self.score.PrintHighScore()


	def menu(self, username):
		self.load_scores()
		print(f"Welcome, {username}!")
		print("""Menu:\n1. Start Game\n2. Show Top Scores\n3. Log Out""")
		choice = int(input("Enter your choice, or leave blank to cancel: "))
		try:
			if choice == 1:
				print(f"Starting game as {username}...\n")
				self.play_game(username)
			elif choice == 2:
				DiceGame.show_top_scores()
			elif choice == 3:
				return
			else:
				return
		except ValueError:
				print("Invalid choice.")

	def rolls(self, username):
			global points
			global wins
			RoundWin = 0
			RoundLose = 0
			if RoundWin <= 3 and RoundLose <= 3:
				RollUser = random.randint(1, 6)
				RollCPU = random.randint(1, 6)
				print(f"{username} rolled: {RollUser}")
				print(f"CPU rolled: {RollCPU}\n")
				if RollUser > RollCPU:
					print(f"You win this round! {username}")
					RoundWin += 1
					points += 1
				elif RollCPU > RollUser:
					print(f"CPU wins this round!")
					RoundLose += 1
				elif RollCPU == RollUser:
					print("It's a tie!")
			else:
				if RoundWin == 3:
						print(f"You won this stage {username}!\n")
						points += 3
						wins += 1
						print(f"""{username} Total points: {points}, Stages Won: {wins}""")
						print(f"Game over. You won {wins} stage(s) with a total of {points} points.")
						return True
				elif RoundLose == 3:
						print(f"You lost this stage {username}.\n")
						print("Game over. You didn't win any stages.")
						return False