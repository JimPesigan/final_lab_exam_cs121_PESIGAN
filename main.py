from utils import user_manager, dice_game, user, score

game = dice_game.DiceGame()
user = user_manager.UserManager()

def main():
    while True:
        try:
            print("""\nWelcome to Dice Roll Game\n1. Register\n2. Login\n3. Exit""")
    
            choice = int(input("Enter your choice: "))

            if choice == 1:
                user.register()
                main()
            if choice == 2:
                user.login()
        
        except ValueError:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()