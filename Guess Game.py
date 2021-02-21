Heart = 5
Rount = 0

while Heart > 0:
    import random

    Range = random.randint(0,20)

    Heart = Heart - 1
    Rount = Rount + 1
    Chance = int(input("Guess the number : "))

    if Chance < Range:
        CWl = Range - Chance
        print(f"Your guess is {CWl} less than the number..")
    elif chance > Range:
        CWh = Chance - Range
        print(f"Your guess is {CWh} more than the number.")
    else:
        print(f"CORRECT ANSWER after {Rount} guess.. Your score : {120 - Rount*20}")
    if Heart == 0:
        print("!!!!GAME OVER. TRY AGAİN.!!!!")
        break
