from utils import user_manager, dice_game, user, score

game = dice_game.DiceGame()
user = user_manager.UserManager()

def main():
    print("""Welcome to Dice Roll Game")
        1. Rgister
        2. Login
        3. Exit""")
    
    choice = int(input("Enter your choice: "))

    if choice == 1:
        user.register()
        main()
    if choice == 2:
        user.login()

if __name__ == "__main__":
    main()