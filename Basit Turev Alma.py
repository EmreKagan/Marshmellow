TUREV = []

sınır = int(input("İşlemdeki karakter sayısını giriniz : "))

x = int(input("X'in değerini giriniz : "))

while sınır > 0:

    sınır = sınır - 1

    nm = float(input("Kat sayı giriniz : ")) 

    üs = float(input("Bir üs giriniz : "))

    if üs != 0:
        türev = nm*üs*x**(üs-1)
    else:
        türev = 0

    TUREV.append(türev)
    sonuc = sum(TUREV)

print(sonuc)





#if üs != 0:
    #türev = nm*üs*x*(üs-1)
#else:
    #türev = nm




#if üs == 0:
        #print(0)
        #break



#Türev = [0]
#Türevs = Türev.append(türevv)
#sonuc = sum(Türevs)
#print(sonuc)


#nm = float(input("Kat sayı giriniz : "))  

#türevv = nm*üs*x*(üs-1)