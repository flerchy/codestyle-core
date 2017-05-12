print ("Программа вычисления номера подъезда.\nБудьте внимательны при вводе данных.\n")

n_kvartiry = input("Введите номер квартиры...\n")
n_kvartiry = int(n_kvartiry)

kol_etazhey = input("Введите количество этажей в доме...\n")
kol_etazhey = int(kol_etazhey)

kol_kvartir_etazh = input("Введите количество квартир на этаже...\n")
kol_kvartir_etazh = int(kol_kvartir_etazh)

kol_kvart_pod = kol_kvartir_etazh * kol_etazhey
result = n_kvartiry / kol_kvart_pod

if result <= 1:
    print ("Номер подъезда 1")
    x=1
elif result <= 2:
    x=2
    print ("Номер подъезда 2")
elif result <= 3:
    x=3
    print ("Номер подъезда 3")
elif result <= 4:
    x=4
    print ("Номер подъезда 4")
elif result <= 5:
    x=5
    print ("Номер подъезда 5")
elif result <= 6:
    x=6
    print ("Номер подъезда 6")
elif result <= 7:
    x=7
    print ("Номер подъезда 7")
elif result <= 8:
    x=8
    print ("Номер подъезда 8")
elif result <= 9:
    x=9
    print ("Номер подъезда 9")
elif result <= 10:
    x=10
    print ("Номер подъезда 10")
elif result <= 11:
    x=11
    print ("Номер подъезда 11")
elif result <= 12:
    x=12
    print ("Номер подъезда 12")
else:
    print("Карлсон живет на крыше!!!")
    
print ("Все квартиры в этом подъезде:")
       
for n in range(1, kol_kvart_pod+1 ):
    res = n + kol_kvart_pod*(x-1)
    print (int(res), end=" ")
