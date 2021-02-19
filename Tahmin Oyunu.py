Can = 5
Sayac = 0

while Can > 0:
    import random

    Aralık = random.randint(0,10)

    Can = Can - 1
    Sayac = Sayac + 1
    chance = int(input("Sayıyı Tahmin Ediniz : "))

    if chance < Aralık:
        farkK = Aralık - chance
        print(f"Tahmininiz, sayının {farkK} eksiği.")
    elif chance > Aralık:
        farkB = chance - Aralık
        print(f"Tahmininiz, sayının {farkB} fazlası.")
    else:
        print(f"{Sayac} adet tahmin sonucu DOĞRU CEVAP. Punınız {120 - Sayac*20}")
    if Can == 0:
        print("!!!!GAME OVER. TRY AGAİN.!!!!")
        break
