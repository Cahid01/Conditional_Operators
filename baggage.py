#İstifadəçi çamadanın çəkisini və bilet növünü (econom/business) yazır.

#Econom: 23 kq-a qədər pulsuz, 23–32 kq arası 30 AZN əlavə ödəniş.
#Business: 32 kq-a qədər pulsuz.
#32 kq-dan ağır çamadan heç bir biletlə qəbul edilmir.


bilet = input("Bilet növünü daxil edin -(Econom/Business)- : ")
weight = int(input("Çamadanın çəkisini daxil edin: "))
if bilet == "Econom":
    if weight < 23:
        print("Çamadan pulsuzdur!")
    elif weight >= 23 and weight <= 32:
        print("Çamadan üçün 30 AZN əlavə ödəniş!")
    else :
        print("Çamadan qəbul edilmir!")
elif bilet == "Business":
    if weight <= 32:
        print("Çamadan pulsuzdur!")
    else:
        print("Çamadan qəbul edilmir!")
else:
    print("Bilet düzgün deyil!") 