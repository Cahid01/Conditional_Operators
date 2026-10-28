#İstifadəçi yaşını yazır və tələbə olub-olmadığını soruşursunuz (bəli/xeyr). 7 yaşdan kiçiklər üçün bilet pulsuzdur, 
#65 yaşdan böyüklər üçün 4 AZN, tələbələr üçün 5 AZN, qalanları üçün 8 AZN. Bilet qiymətini çap edin.


yas = int(input("Yaşınızı daxil edin: "))
telebe = input("Telebesinz ? (Bəli/Xeyr): ")
if telebe == "Beli":
    print("-----Bilet 5 AZN!-----")
else:
    if yas < 7:
        print("-----Bilet pulsuzdur!-----")
    elif yas > 65:
        print("-----Bilet 4 AZN!-----")
    else:
        print("-----Bilet 8 AZN!-----")                