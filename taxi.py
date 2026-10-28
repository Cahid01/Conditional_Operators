#Gediş 2 AZN-dən başlayır, hər km üçün 0.80 AZN əlavə olunur. 
#Gecə saatlarında (23:00–06:00) qiymət 20% artır. Minimum gediş haqqı 3 AZN-dir. 
#İstifadəçi məsafəni və saatı (0–23) yazır, qiyməti çap edin.



hour = int(input("Saatı daxil edin (0-23) : "))
distance = int(input("Məsafəni daxil edin (KM) : "))
price = 2 + (distance * 0.8)
if price >= 3:
    if  hour <=6 or hour == 23:
        price = price + price * 20 / 100
        print("Gediş haqqı",price, "AZN")
    else:
        print("Gedış haqqı", price ,"AZN")    
else:
    print("Gediş haqqı minimum 3 AZN-dir!")    