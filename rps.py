#İki oyunçu növbə ilə seçimini yazır (daş, qayçı, kağız). 
#Kimin qalib gəldiyini və ya heç-heçə olduğunu çap edin. Yanlış söz yazılıbsa: “Belə seçim yoxdur”.



gamer_1 = input("1 ci oyunçu seçimi (daş, qayçı, kağız): ")
gamer_2 = input("2 ci oyunçu seçimi (daş, qayçı, kağız): ")
if gamer_1 == "daş" and gamer_2 == "qayçı":
    print("Gamer 1 qalib gəldi!")
elif gamer_1 == "daş" and gamer_2 == "kağız":
    print("Gamer 2 qalib gəldi!")
elif gamer_1 == "qayçı" and gamer_2 == "daş":
    print("Gamer 2 qalib gəldi!")   
elif gamer_1 == "qayçı" and gamer_2 == "kağız":
    print("Gamer 1 qalib gəldi!")               
elif gamer_1 == "kağız" and gamer_2 == "daş":   
    print("Gamer 1 qalib gəldi!")
elif gamer_1 == "kağız" and gamer_2 == "qayçı":
    print("Gamer 2 qalib gəldi!")
elif gamer_1 == gamer_2:
    print("Heç-heçə")
else:
    print("Belə seçim yoxdur!")
    
