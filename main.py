from utils import user_manager, dice_game

game = dice_game.DiceGame()
user = user_manager.UserManager()

def main():
    while True:
        game.load_scores()
        user.load_users()
        print("Welcome to Dice Roll Game\n1. Register\n2. Login\n3. Exit")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            user.register()
            main()
        elif choice == 2:
            user.login()
        elif choice == 3:
            return 0
        else:
            print("Invalid choice. Please choose a valid option.")

if __name__ == "__main__":
    main()