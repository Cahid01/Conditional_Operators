#stifadəçi 0–100 arası bal yazır. Qiyməti çap edin:
#91–100: A (Əla), 81–90: B, 71–80: C, 61–70: D, 51–60: E, 0–50: F.
#Bal 0-dan kiçik və ya 100-dən böyükdürsə: “Yanlış bal”.


bal = int(input("Balı daxil edin!: "))
if bal > 91 and bal <= 100:
    print("A")
elif bal >= 81 and bal <=90:
    print("B")
elif bal >= 71 and bal <= 80:
    print("C")
elif bal >= 61 and bal <=70:
    print("D")
elif bal >= 51 and bal<=60:
    print("E")
elif bal >= 0 and bal <= 50:
    print("F")
else :
    print("Bal yalnışdır!")
         