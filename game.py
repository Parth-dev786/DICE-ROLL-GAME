from random_num import roll_dice
def play_round():
    while True:
        user = input("roll dice? (yes/no):" ).lower()
        if user == 'yes':
            user = roll_dice()
            computer = roll_dice()

            print("You rolled:",user)
            print("computer rolled:",computer)

            if user>computer:
                print("You win")
            elif user<computer:
                print("computer win")
            else:
                print("its a Draw")
        elif user == 'no':
            print("game over")
        else:
            print("yes or no")