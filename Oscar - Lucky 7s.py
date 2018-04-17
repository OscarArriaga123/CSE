import random
money = 15
answer = 7
rounds = 0


while money > 0:
    dice1 = random.randint(1, 6)
    print(dice1)
    dice2 = random.randint(1, 6)
    print(dice2)
    print("You rolled a %s" % dice1)
    print("and you also rolled a %s" % dice2)

    print(dice1+dice2)
    if (dice1+dice2) == answer:
        money += 4
    else:
        money -= 1
        print(money)

        print("You have %s dollars left" % money)
        print("You have played over %s rounds" % rounds)
        rounds += 1
