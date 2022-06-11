def gamblers_ruin():
    import random

    pot_of_cash = float(input("Enter the amount of money you have: "))
    cash_target = float(input("Enter the amount of money you want to reach: "))

    round_num = 1

    while pot_of_cash > 0:
        print("round number:", round_num, ":", "Cash Total:", pot_of_cash)
        num = []

        for dice in range(1, 3):
            dice = random.randint(1, 6)
            num.append(dice)
            print(num)

        if sum(num) < 6:
            pot_of_cash += 1
        if sum(num) >= 6:
            pot_of_cash -= 1

        if pot_of_cash == cash_target:
            print("You got your target balance!")

            print("Would you like to play again? (y/n)")
            if input() == "y":
                gamblers_ruin()
            if input() == "n":
                print("Thanks for playing!")

        if pot_of_cash == 0:
            # Printing the string "You lost all your money!"
            print("You lost all your money!")
        round_num += 1


gamblers_ruin()
